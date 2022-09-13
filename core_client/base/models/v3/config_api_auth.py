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

    enable: Optional[bool]
    disable_localhost: Optional[bool]
    username: Optional[str]
    password: Optional[str]
    jwt: Optional[ConfigApiAuthJwt]
    auth0: Optional[ConfigApiAuthAuth0]
