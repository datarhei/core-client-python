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

    enable: bool | None = None
    address: str | None = None
    passphrase: str | None = None
    token: str | None = None
    log: ConfigSrtLog | None = None
