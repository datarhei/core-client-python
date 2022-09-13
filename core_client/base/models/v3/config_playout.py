from pydantic import BaseModel
from typing import Optional


class ConfigPlayout(BaseModel):
    """
    {
        "enable": False,
        "min_port": 0,
        "max_port": 0
    }
    """

    enable: Optional[bool]
    min_port: Optional[int]
    max_port: Optional[int]
