from pydantic import BaseModel
from typing import List, Optional


class ConfigStorageDiskCacheTypes(BaseModel):
    """
    {
        "allow": [],
        "block": [".m3u8"]
    }
    """

    allow: Optional[List[str]] = None
    block: Optional[List[str]] = None
