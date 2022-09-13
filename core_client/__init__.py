import httpx
import functools
import importlib
import pkgutil
import base64
import json
from datetime import datetime
from httpx import InvalidURL as HttpInvalidURL, HTTPError
from pydantic import HttpUrl, ValidationError as PydanticValidationError, validate_arguments

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
        self.retries = retries
        self.timeout = timeout

    def _access_token(self, response: Token = None):
        if response:
            self.token_expire = json.loads(
                (base64.b64decode(response.access_token.split(".")[1])).decode("utf-8")
            )["exp"]
            self.access_token = response.access_token

    def _refresh_token(self):
        if self.refresh_token:
            _headers = self.headers
            _headers["authorization"] = f"Bearer {self.refresh_token}"
            r_refresh_token = httpx.get(
                url=f"{self.base_url}/api/login/refresh",
                headers=_headers,
                # failed login delay: 5s
                timeout=10.0,
            )
            if r_refresh_token.status_code == 200:
                response = AccessToken(**r_refresh_token.json())
                self._access_token(response)
                return True
        return False

    def _token_expired(self):
        if datetime.fromtimestamp(self.token_expire) > datetime.now():
            return False
        return True

    def _get_headers(self):
        _headers = self.headers
        if self.refresh_token:
            if self._token_expired():
                self._refresh_token()
            _headers["authorization"] = f"Bearer {self.access_token}"
            return _headers
        return _headers

    def login(self):
        r_about = httpx.get(url=f"{self.base_url}/api")
        if r_about.status_code == 200:
            try:
                about = About(**r_about.json())
            except PydanticValidationError:
                raise HttpInvalidURL(f'"{self.base_url}/api"')
            if about.auths and "localjwt" in about.auths and self.username and self.password:
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
                        self._access_token(response)
                        self.refresh_token = response.refresh_token
                        return response
                    except PydanticValidationError:
                        return Token()
                raise HTTPError(f'"Authorization failed", {r_login.status_code}')
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
            AsyncClient._add_proxy_method(submodule_info.name, submodule.asyncio)
        if hasattr(submodule, "sync"):
            Client._add_proxy_method(submodule_info.name, submodule.sync)
