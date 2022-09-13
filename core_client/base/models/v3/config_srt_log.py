from pydantic import BaseModel
from typing import Optional, List


class ConfigSrtLog(BaseModel):
    """
    {
        "enable": False,
        "topics": []
    }
    """

    enable: Optional[bool]
    topics: Optional[List[str]]
