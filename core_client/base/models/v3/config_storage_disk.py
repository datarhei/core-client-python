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

    dir: str | None = None
    max_size_mbytes: int | None = None
    cache: ConfigStorageDiskCache | None = None
