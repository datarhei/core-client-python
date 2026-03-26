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

    disk: ConfigStorageDisk | None = None
    memory: ConfigStorageMemory | None = None
    cors: ConfigStorageCors | None = None
    mimetypes_file: str | None = None
    s3: list[ConfigStorageS3] | None = None
