from pydantic import BaseModel
from typing import List, Optional


class ConfigStorageDiskCacheTypes(BaseModel):
    """
    {
        "allow": [],
        "block": [".m3u8"]
    }
    """

    allow: Optional[List[str]]
    block: Optional[List[str]]
