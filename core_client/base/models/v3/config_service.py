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

    enable: Optional[bool]
    token: Optional[str]
    url: Optional[str]
