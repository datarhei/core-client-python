from pydantic import BaseModel
from typing import List, Optional


class ConfigStorageDiskCacheTypes(BaseModel):
    """
    {
        "allow": [],
        "block": [".m3u8"]
    }
    """

    allow: list[str] | None = None
    block: list[str] | None = None
