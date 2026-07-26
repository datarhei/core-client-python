import asyncio
import httpx
import functools
import importlib
import pkgutil
import threading
import jwt
from datetime import datetime
from httpx import InvalidURL as HttpInvalidURL, HTTPError
from pydantic import HttpUrl, ValidationError as PydanticValidationError, validate_call

from . import base
from .models import Client as ClientModel
from .base.models import Token, AccessToken, About, Error
from .exceptions import CoreAPIError


class Client:
    @validate_call()
    def __init__(
        self,
        base_url: HttpUrl,
        username: str = None,
        password: str = None,
        domain: str = None,
        access_token: str = None,
        refresh_token: str = None,
        auth0_token: str = None,
        retries: int = 3,
        timeout: float = 10.0,
        raise_on_error: bool = False,
    ):
        self.headers = {
            "accept": "application/json",
            "content-type": "application/json",
        }
        if str(base_url).endswith("/"):
            self.base_url = str(base_url)[:-1]
        else:
            self.base_url = str(base_url)
        self.username = username
        self.password = password
        self.domain = domain
        self.access_token = access_token
        self.refresh_token = refresh_token
        self.access_token_expires_at = None
        self.refresh_token_expires_at = None
        self.auth0_token = auth0_token
        self.retries = retries
        self.timeout = timeout
        self.raise_on_error = raise_on_error
        # Guards the token refresh/login path against concurrent callers (§2.1).
        self._refresh_lock = threading.Lock()
        # Lazily created pooled httpx.Client reused across requests (§2.3/§2.4).
        self._http_client = None

    def _pooled_http_client(self):
        if self._http_client is None:
            transport = httpx.HTTPTransport(retries=self.retries)
            self._http_client = httpx.Client(transport=transport, http2=True)
        return self._http_client

    def close(self):
        """Close the pooled httpx client, if one was created."""
        if self._http_client is not None:
            self._http_client.close()
            self._http_client = None

    def __enter__(self):
        return self

    def __exit__(self, *exc):
        self.close()

    def _basic_login(self):
        domain_param = f"?domain={self.domain}" if self.domain else ""
        r_login = httpx.post(
            url=f"{self.base_url}/api/login{domain_param}",
            json={
                "username": f"{self.username}",
                "password": f"{self.password}",
            },
            # failed login delay: 5s
            timeout=10.0,
        )
        if r_login.status_code == 200:
            try:
                response = Token(**r_login.json())
                self._set_access_token_expires_at(response)
                self.refresh_token = response.refresh_token
                self._set_refresh_token_expires_at(response)
                return response
            except PydanticValidationError:
                return Token()
        else:
            raise HTTPError("Authorization failed")

    def _auth0_login(self):
        _headers = self.headers.copy()
        _headers["authorization"] = f"Bearer {self.auth0_token}"
        r_login = httpx.post(
            url=f"{self.base_url}/api/login",
            headers=_headers,
            # failed login delay: 5s
            timeout=10.0,
        )
        if r_login.status_code == 200:
            try:
                response = Token(**r_login.json())
                self._set_access_token_expires_at(response)
                self.refresh_token = response.refresh_token
                self._set_refresh_token_expires_at(response)
                return response
            except PydanticValidationError:
                return Token()
        else:
            raise HTTPError("Authorization failed")

    def _set_access_token_expires_at(self, response: Token = None):
        if response and response.access_token:
            try:
                self.access_token_expires_at = jwt.decode(
                    response.access_token, options={"verify_signature": False}
                )["exp"]
            except (
                AttributeError,
                IndexError,
                KeyError,
                TypeError,
                jwt.exceptions.PyJWTError,
            ):
                raise HTTPError("Authorization failed")
            self.access_token = response.access_token
            return self.access_token_expires_at

    def _access_token_is_expired(self):
        if not self.access_token:
            return True
        if not self.access_token_expires_at:
            try:
                self._set_access_token_expires_at(Token(access_token=self.access_token))
            except (PydanticValidationError, TypeError, HTTPError):
                return True
        if datetime.fromtimestamp(self.access_token_expires_at) > datetime.now():
            return False
        return True

    def _set_refresh_token_expires_at(self, response: Token = None):
        if response and response.refresh_token:
            try:
                self.refresh_token_expires_at = jwt.decode(
                    response.refresh_token, options={"verify_signature": False}
                )["exp"]
            except (
                AttributeError,
                IndexError,
                KeyError,
                TypeError,
                jwt.exceptions.PyJWTError,
            ):
                raise HTTPError("Authorization failed")
            self.refresh_token = response.refresh_token
            return self.refresh_token_expires_at

    def _refresh_token_is_expired(self):
        if not self.refresh_token:
            return True
        if not self.refresh_token_expires_at:
            try:
                self._set_refresh_token_expires_at(Token(refresh_token=self.refresh_token))
            except (PydanticValidationError, TypeError, HTTPError):
                return True
        if datetime.fromtimestamp(self.refresh_token_expires_at) > datetime.now():
            return False
        return True

    def _refresh_access_token(self):
        if self.refresh_token:
            _headers = self.headers.copy()
            _headers["authorization"] = f"Bearer {self.refresh_token}"
            r_refresh_access_token = httpx.get(
                url=f"{self.base_url}/api/login/refresh",
                headers=_headers,
                # failed login delay: 5s
                timeout=10.0,
            )
            if r_refresh_access_token.status_code == 200:
                response = AccessToken(**r_refresh_access_token.json())
                if response.access_token is not None:
                    self._set_access_token_expires_at(response)
            else:
                self._basic_login()
        else:
            self._basic_login()

    def _get_headers(self):
        _headers = self.headers.copy()
        if (self.username and self.password) or self.access_token or self.refresh_token or self.auth0_token:
            with self._refresh_lock:
                if (
                    self.refresh_token
                    and self._refresh_token_is_expired() is False
                    and self._access_token_is_expired() is True
                ):
                    self._refresh_access_token()
                elif self.refresh_token and self._refresh_token_is_expired() is True:
                    self.login()
            if self.access_token:
                _headers["authorization"] = f"Bearer {self.access_token}"
        return _headers

    def token(self):
        expires_at = None
        if self.access_token_expires_at is not None:
            expires_at = int(self.access_token_expires_at)
        return Token(
            access_token=self.access_token,
            refresh_token=self.refresh_token,
            expires_at=expires_at,
        )

    def refresh(self):
        """Refresh the access token now (proactive), under the refresh lock.

        Uses the existing refresh-token path with re-login fallback. Unlike
        ``login()`` this makes no ``GET /api`` preflight, so it is suited for
        periodic background refresh in long-running applications.
        """
        with self._refresh_lock:
            self._refresh_access_token()
        return self.token()

    def login(self):
        r_about = httpx.get(url=f"{self.base_url}/api", timeout=self.timeout)
        if r_about.status_code == 200:
            try:
                about = About(**r_about.json())
            except PydanticValidationError:
                raise HttpInvalidURL(f'"{self.base_url}/api"')
            if about.auths and "localjwt" in about.auths:
                if self.refresh_token:
                    try:
                        self._refresh_access_token()
                        return self.token()
                    except (PydanticValidationError, TypeError):
                        raise HTTPError("Authorization failed")
                elif self.auth0_token:
                    self._auth0_login()
                    return self.token()
                elif self.username and self.password:
                    self._basic_login()
                    return self.token()
                elif self.access_token and not self.refresh_token and not (self.username and self.password):
                    try:
                        response = Token(access_token=self.access_token)
                        self._set_access_token_expires_at(response)
                        return response
                    except (PydanticValidationError, TypeError):
                        return Token()
                elif (
                    not self.access_token and not self.refresh_token and not (self.username and self.password)
                ):
                    return Token()
                else:
                    raise HTTPError("Authorization failed")
            return Token()
        raise HTTPError(f'"{self.base_url}/api", {r_about.status_code}')

    def _raise_if_error(self, result):
        if self.raise_on_error and isinstance(result, Error):
            raise CoreAPIError(result)
        return result

    @classmethod
    def _make_proxy_method(cls, function):
        @functools.wraps(function)
        def proxy_method(self, **kwargs):
            def call():
                call_kwargs = dict(kwargs)
                call_kwargs["client"] = ClientModel(
                    base_url=self.base_url,
                    headers=self._get_headers(),
                    retries=self.retries,
                    timeout=self.timeout,
                    http_client=self._pooled_http_client(),
                )
                return function(**call_kwargs)

            result = call()
            # One-shot retry on a 401: the token may have been invalidated
            # server-side (restart / secret rotation). Invalidate and retry once.
            if isinstance(result, Error) and result.code == 401:
                with self._refresh_lock:
                    self.access_token = None
                result = call()
            return self._raise_if_error(result)

        return proxy_method

    @classmethod
    def _add_proxy_method(cls, method_name, function):
        proxy_method = cls._make_proxy_method(function)
        if not hasattr(cls, method_name):
            setattr(cls, method_name, proxy_method)


class AsyncClient(Client):
    def _get_async_refresh_lock(self):
        lock = getattr(self, "_async_refresh_lock", None)
        if lock is None:
            lock = asyncio.Lock()
            self._async_refresh_lock = lock
        return lock

    def _pooled_async_http_client(self):
        client = getattr(self, "_async_http_client", None)
        if client is None:
            transport = httpx.AsyncHTTPTransport(retries=self.retries)
            client = httpx.AsyncClient(transport=transport, http2=True)
            self._async_http_client = client
        return client

    async def aclose(self):
        """Close the pooled async httpx client, if one was created."""
        client = getattr(self, "_async_http_client", None)
        if client is not None:
            await client.aclose()
            self._async_http_client = None

    async def __aenter__(self):
        return self

    async def __aexit__(self, *exc):
        await self.aclose()

    async def _abasic_login(self):
        domain_param = f"?domain={self.domain}" if self.domain else ""
        async with httpx.AsyncClient(http2=True) as client:
            r_login = await client.post(
                url=f"{self.base_url}/api/login{domain_param}",
                json={"username": f"{self.username}", "password": f"{self.password}"},
                timeout=10.0,
            )
        if r_login.status_code == 200:
            try:
                response = Token(**r_login.json())
                self._set_access_token_expires_at(response)
                self.refresh_token = response.refresh_token
                self._set_refresh_token_expires_at(response)
                return response
            except PydanticValidationError:
                return Token()
        else:
            raise HTTPError("Authorization failed")

    async def _aauth0_login(self):
        _headers = self.headers.copy()
        _headers["authorization"] = f"Bearer {self.auth0_token}"
        async with httpx.AsyncClient(http2=True) as client:
            r_login = await client.post(
                url=f"{self.base_url}/api/login", headers=_headers, timeout=10.0
            )
        if r_login.status_code == 200:
            try:
                response = Token(**r_login.json())
                self._set_access_token_expires_at(response)
                self.refresh_token = response.refresh_token
                self._set_refresh_token_expires_at(response)
                return response
            except PydanticValidationError:
                return Token()
        else:
            raise HTTPError("Authorization failed")

    async def _arefresh_access_token(self):
        if self.refresh_token:
            _headers = self.headers.copy()
            _headers["authorization"] = f"Bearer {self.refresh_token}"
            async with httpx.AsyncClient(http2=True) as client:
                r_refresh = await client.get(
                    url=f"{self.base_url}/api/login/refresh", headers=_headers, timeout=10.0
                )
            if r_refresh.status_code == 200:
                response = AccessToken(**r_refresh.json())
                if response.access_token is not None:
                    self._set_access_token_expires_at(response)
            else:
                await self._abasic_login()
        else:
            await self._abasic_login()

    async def alogin(self):
        async with httpx.AsyncClient(http2=True) as client:
            r_about = await client.get(url=f"{self.base_url}/api", timeout=self.timeout)
        if r_about.status_code == 200:
            try:
                about = About(**r_about.json())
            except PydanticValidationError:
                raise HttpInvalidURL(f'"{self.base_url}/api"')
            if about.auths and "localjwt" in about.auths:
                if self.refresh_token:
                    try:
                        await self._arefresh_access_token()
                        return self.token()
                    except (PydanticValidationError, TypeError):
                        raise HTTPError("Authorization failed")
                elif self.auth0_token:
                    await self._aauth0_login()
                    return self.token()
                elif self.username and self.password:
                    await self._abasic_login()
                    return self.token()
                elif self.access_token and not self.refresh_token and not (self.username and self.password):
                    try:
                        response = Token(access_token=self.access_token)
                        self._set_access_token_expires_at(response)
                        return response
                    except (PydanticValidationError, TypeError):
                        return Token()
                elif (
                    not self.access_token and not self.refresh_token and not (self.username and self.password)
                ):
                    return Token()
                else:
                    raise HTTPError("Authorization failed")
            return Token()
        raise HTTPError(f'"{self.base_url}/api", {r_about.status_code}')

    async def arefresh(self):
        """Async counterpart of :meth:`Client.refresh`."""
        async with self._get_async_refresh_lock():
            await self._arefresh_access_token()
        return self.token()

    async def _aget_headers(self):
        _headers = self.headers.copy()
        if (self.username and self.password) or self.access_token or self.refresh_token or self.auth0_token:
            async with self._get_async_refresh_lock():
                if (
                    self.refresh_token
                    and self._refresh_token_is_expired() is False
                    and self._access_token_is_expired() is True
                ):
                    await self._arefresh_access_token()
                elif self.refresh_token and self._refresh_token_is_expired() is True:
                    await self.alogin()
            if self.access_token:
                _headers["authorization"] = f"Bearer {self.access_token}"
        return _headers

    @classmethod
    def _make_proxy_method(cls, function):
        @functools.wraps(function)
        async def proxy_method(self, *args, **kwargs):
            async def call():
                call_kwargs = dict(kwargs)
                call_kwargs["client"] = ClientModel(
                    base_url=self.base_url,
                    headers=await self._aget_headers(),
                    retries=self.retries,
                    timeout=self.timeout,
                    http_client=self._pooled_async_http_client(),
                )
                return await function(*args, **call_kwargs)

            result = await call()
            if isinstance(result, Error) and result.code == 401:
                async with self._get_async_refresh_lock():
                    self.access_token = None
                result = await call()
            return self._raise_if_error(result)

        return proxy_method

    @classmethod
    def _make_stream_method(cls, function):
        """Wrap an ``asyncio_stream`` module function as an async-generator method.

        Unlike ``_make_proxy_method`` this is a plain (non-async) method that
        returns an async generator, so callers do ``async for ev in client.x(...)``.
        Headers are fetched fresh when iteration starts (connection time), and
        ``_raise_if_error`` is not applied — streaming errors surface as
        ``CoreAPIError`` on connect (see ``_stream``).
        """

        @functools.wraps(function)
        def stream_method(self, **kwargs):
            async def agen():
                client = ClientModel(
                    base_url=self.base_url,
                    headers=await self._aget_headers(),
                    retries=self.retries,
                    timeout=self.timeout,
                )
                async for item in function(client=client, **kwargs):
                    yield item

            return agen()

        return stream_method

    @classmethod
    def _add_stream_method(cls, method_name, function):
        if not hasattr(cls, method_name):
            setattr(cls, method_name, cls._make_stream_method(function))


for module_info in pkgutil.walk_packages(path=base.__path__, prefix=f"{base.__name__}."):
    try:
        if not module_info.ispkg:
            continue

        module = importlib.import_module(module_info.name)
        sub_prefix = f"{module.__name__}."
        for submodule_info in pkgutil.walk_packages(path=module.__path__, prefix=sub_prefix):
            submodule = importlib.import_module(submodule_info.name)
            method_name = submodule_info.name.split(".")[-1]
            if hasattr(submodule, "asyncio_stream"):
                AsyncClient._add_stream_method(method_name, submodule.asyncio_stream)
            if hasattr(submodule, "asyncio"):
                AsyncClient._add_proxy_method(method_name, submodule.asyncio)
            if hasattr(submodule, "sync"):
                Client._add_proxy_method(method_name, submodule.sync)

    except Exception as e:
        print(f"  ERROR processing {module_info.name}: {e}")


_METHOD_ALIASES = {
    "v3_process_get_report": "v3_report_get_process",
    "v3_iam_put_user_policy_list": "v3_iam_put_user_policy",
}

for alias, target in _METHOD_ALIASES.items():
    if hasattr(Client, target) and not hasattr(Client, alias):
        setattr(Client, alias, getattr(Client, target))
    if hasattr(AsyncClient, target) and not hasattr(AsyncClient, alias):
        setattr(AsyncClient, alias, getattr(AsyncClient, target))


# New canonical class names for datarhei MediaCore branding.
MediaCoreClient = Client
AsyncMediaCoreClient = AsyncClient
