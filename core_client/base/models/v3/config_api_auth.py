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

    enable: Optional[bool] = None
    disable_localhost: Optional[bool] = None
    username: Optional[str] = None
    password: Optional[str] = None
    jwt: Optional[ConfigApiAuthJwt] = None
    auth0: Optional[ConfigApiAuthAuth0] = None
