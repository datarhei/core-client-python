import httpx
import functools
import importlib
import pkgutil
import jwt
from datetime import datetime
from httpx import InvalidURL as HttpInvalidURL, HTTPError
from pydantic import (
    HttpUrl,
    ValidationError as PydanticValidationError,
    validate_arguments,
)

from . import base
from .models import Client as ClientModel
from .base.models import Token, AccessToken, About


class Client:
    @validate_arguments()
    def __init__(
        self,
        base_url: HttpUrl,
        username: str = None,
        password: str = None,
        access_token: str = None,
        refresh_token: str = None,
        auth0_token: str = None,
        retries: int = 3,
        timeout: float = 10.0,
    ):
        self.headers = {
            "accept": "application/json",
            "content-type": "application/json",
        }
        if base_url.endswith("/"):
            self.base_url = base_url[:-1]
        else:
            self.base_url = base_url
        self.username = username
        self.password = password
        self.access_token = access_token
        self.refresh_token = refresh_token
        self.access_token_expires_at = None
        self.refresh_token_expires_at = None
        self.auth0_token = auth0_token
        self.retries = retries
        self.timeout = timeout

    def _basic_login(self):
        r_login = httpx.post(
            url=f"{self.base_url}/api/login",
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
                return response
            except PydanticValidationError:
                return Token()
        else:
            raise HTTPError("Authorization failed")

    def _auth0_login(self):
        _headers = self.headers
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
        if response:
            try:
                self.access_token_expires_at = jwt.decode(
                    response.access_token, options={"verify_signature": False}
                )["exp"]
            except (AttributeError, IndexError):
                raise HTTPError("Authorization failed")
            self.access_token = response.access_token
            return self.access_token_expires_at

    def _access_token_is_expired(self):
        if not self.access_token_expires_at:
            self._set_access_token_expires_at(
                Token(access_token=self.access_token)
            )
        if (
            datetime.fromtimestamp(self.access_token_expires_at)
            > datetime.now()
        ):
            return False
        return True

    def _set_refresh_token_expires_at(self, response: Token = None):
        if response:
            try:
                self.refresh_token_expires_at = jwt.decode(
                    response.refresh_token, options={"verify_signature": False}
                )["exp"]
            except (AttributeError, IndexError):
                raise HTTPError("Authorization failed")
            self.refresh_token = response.refresh_token
            return self.refresh_token_expires_at

    def _refresh_token_is_expired(self):
        if not self.refresh_token_expires_at:
            self._set_refresh_token_expires_at(
                Token(refresh_token=self.refresh_token)
            )
        if (
            datetime.fromtimestamp(self.refresh_token_expires_at)
            > datetime.now()
        ):
            return False
        return True

    def _refresh_access_token(self):
        if self.refresh_token:
            _headers = self.headers
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
        _headers = self.headers
        if (
            self.refresh_token
            and self._refresh_token_is_expired() is False
            and self._access_token_is_expired() is True
        ):
            self._refresh_access_token()
        elif self.refresh_token and self._refresh_token_is_expired() is True:
            self.login()
        _headers["authorization"] = f"Bearer {self.access_token}"
        return _headers

    def token(self):
        return Token(
            access_token=self.access_token,
            refresh_token=self.refresh_token,
            expires_at=int(self.access_token_expires_at),
        )

    def login(self):
        r_about = httpx.get(url=f"{self.base_url}/api")
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
                elif (
                    self.access_token
                    and not self.refresh_token
                    and not (self.username and self.password)
                ):
                    try:
                        response = Token(access_token=self.access_token)
                        self._set_access_token_expires_at(response)
                        return response
                    except (PydanticValidationError, TypeError):
                        return Token()
                else:
                    raise HTTPError("Authorization failed")
            return Token()
        raise HTTPError(f'"{self.base_url}/api", {r_about.status_code}')

    @classmethod
    def _make_proxy_method(cls, function):
        @functools.wraps(function)
        def proxy_method(self, **kwargs):
            kwargs["client"] = ClientModel(
                base_url=self.base_url,
                headers=self._get_headers(),
                retries=self.retries,
                timeout=self.timeout,
            )
            return function(**kwargs)

        return proxy_method

    @classmethod
    def _add_proxy_method(cls, method_name, function):
        proxy_method = cls._make_proxy_method(function)
        if not hasattr(cls, method_name):
            setattr(cls, method_name, proxy_method)


class AsyncClient(Client):
    @classmethod
    def _make_proxy_method(cls, function):
        @functools.wraps(function)
        async def proxy_method(self, *args, **kwargs):
            kwargs["client"] = ClientModel(
                base_url=self.base_url,
                headers=self._get_headers(),
                retries=self.retries,
                timeout=self.timeout,
            )
            return await function(*args, **kwargs)

        return proxy_method


for module_info in pkgutil.walk_packages(base.__path__):
    module_name = f"{base.__name__}.{module_info.name}"
    module = importlib.import_module(module_name)
    for submodule_info in pkgutil.walk_packages(module.__path__):
        submodule_name = f"{module_name}.{submodule_info.name}"
        submodule = importlib.import_module(submodule_name)
        if hasattr(submodule, "asyncio"):
            AsyncClient._add_proxy_method(
                submodule_info.name, submodule.asyncio
            )
        if hasattr(submodule, "sync"):
            Client._add_proxy_method(submodule_info.name, submodule.sync)
