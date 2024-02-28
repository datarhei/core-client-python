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

    enable: Optional[bool] = None
    token: Optional[str] = None
    url: Optional[str] = None
