from pydantic import BaseModel
from typing import Optional

from . import ConfigStorageMemoryAuth, ConfigStorageMemoryBackup


class ConfigStorageMemory(BaseModel):
    """
    {
        "auth": ConfigStorageMemoryAuth,
        + "backup": ConfigStorageMemoryBackup,
        "max_size_mbytes": 0,
        "purge": False
    }
    """

    auth: Optional[ConfigStorageMemoryAuth]
    backup: Optional[ConfigStorageMemoryBackup]
    max_size_mbytes: Optional[int]
    purge: Optional[bool]
