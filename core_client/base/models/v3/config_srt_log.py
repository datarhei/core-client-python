from pydantic import BaseModel
from typing import Optional, List


class ConfigSrtLog(BaseModel):
    """
    {
        "enable": False,
        "topics": []
    }
    """

    enable: bool | None = None
    topics: list[str] | None = None
