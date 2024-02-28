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

    enable: Optional[bool] = None
    enable_tls: Optional[bool] = None
    address: Optional[str] = None
    address_tls: Optional[str] = None
    app: Optional[str] = None
    token: Optional[str] = None
