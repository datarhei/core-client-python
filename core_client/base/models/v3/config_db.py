from pydantic import BaseModel
from typing import Optional


class ConfigDb(BaseModel):
    """
    {
        "dir": "/core/config"
    }
    """

    dir: str | None = None
