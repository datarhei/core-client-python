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

    enable: Optional[bool]
    enable_tls: Optional[bool]
    address: Optional[str]
    address_tls: Optional[str]
    app: Optional[str]
    token: Optional[str]
