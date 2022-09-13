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

    enable: Optional[bool]
    max_size_mbytes: Optional[int]
    ttl_seconds: Optional[int]
    max_file_size_mbytes: Optional[int]
    types: Optional[Union[List[str], ConfigStorageDiskCacheTypes]]
