from pydantic import BaseModel
from typing import Optional, List, Union

from . import ConfigStorageDiskCacheTypes


class ConfigStorageDiskCache(BaseModel):
    """
    # v3:
    {
        "enable": True,
        "max_size_mbytes": 0,
        "ttl_seconds": 300,
        "max_file_size_mbytes": 1,
        "types": ConfigStorageDiskCacheTypes
    }

    # v2:
    {
        "enable": True,
        "max_size_mbytes": 0,
        "ttl_seconds": 300,
        "max_file_size_mbytes": 1,
        "types": []
    }
    """

    enable: bool | None = None
    max_size_mbytes: int | None = None
    ttl_seconds: int | None = None
    max_file_size_mbytes: int | None = None
    types: list[str] | ConfigStorageDiskCacheTypes | None = None
