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

    auth: Optional[ConfigStorageMemoryAuth] = None
    backup: Optional[ConfigStorageMemoryBackup] = None
    max_size_mbytes: Optional[int] = None
    purge: Optional[bool] = None
