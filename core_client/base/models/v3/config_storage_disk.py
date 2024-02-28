from pydantic import BaseModel
from typing import Optional

from . import ConfigStorageDiskCache


class ConfigStorageDisk(BaseModel):
    """
    {
        "dir": "/core/data",
        "max_size_mbytes": 0,
        "cache": ConfigStorageDiskCache
    }
    """

    dir: Optional[str] = None
    max_size_mbytes: Optional[int] = None
    cache: Optional[ConfigStorageDiskCache] = None
