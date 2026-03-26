from pydantic import BaseModel
from typing import Optional


class ConfigService(BaseModel):
    """
    {
        "enable": False,
        "token": "",
        "url": "https://service.datarhei.com"
    }
    """

    enable: bool | None = None
    token: str | None = None
    url: str | None = None
