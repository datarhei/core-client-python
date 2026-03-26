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

    enable: bool | None = None
    min_port: int | None = None
    max_port: int | None = None
