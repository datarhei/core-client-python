from pydantic import BaseModel
from typing import Optional

from . import ConfigApiAuthAuth0, ConfigApiAuthJwt


class ConfigApiAuth(BaseModel):
    """
    {
        "enable": False,
        "disable_localhost": False,
        "username": "",
        "password": "",
        "jwt": ConfigApiAuthJwt,
        "auth0": ConfigApiAuthAuth0
    }
    """

    enable: bool | None = None
    disable_localhost: bool | None = None
    username: str | None = None
    password: str | None = None
    jwt: ConfigApiAuthJwt | None = None
    auth0: ConfigApiAuthAuth0 | None = None
