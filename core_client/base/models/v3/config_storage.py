from pydantic import BaseModel
from typing import Optional

from . import (
    ConfigStorageDisk,
    ConfigStorageMemory,
    ConfigStorageCors,
    ConfigStorageS3,
)


class ConfigStorage(BaseModel):
    """
    {
        "disk": ConfigStorageDisk,
        "memory": ConfigStorageMemory,
        "cors": ConfigStorageCors,
        "mimetypes_file": "./mime.types"
    }
    """

    """
    + {
        "s3": [ConfigStorageS3]
    }
    """

    disk: Optional[ConfigStorageDisk] = None
    memory: Optional[ConfigStorageMemory] = None
    cors: Optional[ConfigStorageCors] = None
    mimetypes_file: Optional[str] = None
    s3: Optional[list[ConfigStorageS3]] = None
