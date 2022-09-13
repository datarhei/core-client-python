from pydantic import BaseModel
from typing import Optional

from . import ConfigStorageMemoryAuth


class ConfigStorageMemory(BaseModel):
    """
    {
        "auth": ConfigStorageMemoryAuth,
        "max_size_mbytes": 0,
        "purge": False
    }
    """

    auth: Optional[ConfigStorageMemoryAuth]
    max_size_mbytes: Optional[int]
    purge: Optional[bool]
