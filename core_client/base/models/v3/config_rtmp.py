from pydantic import BaseModel
from typing import Optional


class ConfigRtmp(BaseModel):
    """
    {
        "enable": False,
        "enable_tls": False,
        "address": ":1935",
        "address_tls": ":1936",
        "app": "/",
        "token": ""
    }
    """

    enable: bool | None = None
    enable_tls: bool | None = None
    address: str | None = None
    address_tls: str | None = None
    app: str | None = None
    token: str | None = None
