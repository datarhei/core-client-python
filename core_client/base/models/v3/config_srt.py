from pydantic import BaseModel
from typing import Optional

from . import ConfigSrtLog


class ConfigSrt(BaseModel):
    """
    {
        "enable": False,
        "address": ":6000",
        "passphrase": "",
        "token": "",
        "log": ConfigSrtLog
    }
    """

    enable: Optional[bool] = None
    address: Optional[str] = None
    passphrase: Optional[str] = None
    token: Optional[str] = None
    log: Optional[ConfigSrtLog] = None
