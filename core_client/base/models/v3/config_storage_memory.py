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

    auth: ConfigStorageMemoryAuth | None = None
    backup: ConfigStorageMemoryBackup | None = None
    max_size_mbytes: int | None = None
    purge: bool | None = None
