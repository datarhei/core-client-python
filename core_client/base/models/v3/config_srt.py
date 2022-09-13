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

    enable: Optional[bool]
    address: Optional[str]
    passphrase: Optional[str]
    token: Optional[str]
    log: Optional[ConfigSrtLog]
