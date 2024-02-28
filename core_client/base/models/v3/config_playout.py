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

    enable: Optional[bool] = None
    min_port: Optional[int] = None
    max_port: Optional[int] = None
