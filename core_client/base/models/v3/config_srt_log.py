from pydantic import BaseModel
from typing import Optional, List


class ConfigSrtLog(BaseModel):
    """
    {
        "enable": False,
        "topics": []
    }
    """

    enable: Optional[bool] = None
    topics: Optional[List[str]] = None
