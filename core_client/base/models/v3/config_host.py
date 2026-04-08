from pydantic import BaseModel
from typing import Optional, List


class ConfigHost(BaseModel):
    """
    {
        "name": ["86.103.229.239"],
        "auto": True
    }
    """

    name: list[str] | None = None
    auto: bool | None = None
