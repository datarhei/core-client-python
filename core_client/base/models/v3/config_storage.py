from pydantic import BaseModel
from typing import Optional

from . import ConfigStorageDisk, ConfigStorageMemory, ConfigStorageCors


class ConfigStorage(BaseModel):
    """
    {
        "disk": ConfigStorageDisk,
        "memory": ConfigStorageMemory,
        "cors": ConfigStorageCors,
        "mimetypes_file": "./mime.types"
    }
    """

    disk: Optional[ConfigStorageDisk]
    memory: Optional[ConfigStorageMemory]
    cors: Optional[ConfigStorageCors]
    mimetypes_file: Optional[str]
