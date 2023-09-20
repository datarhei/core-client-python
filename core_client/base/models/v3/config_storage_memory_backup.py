from pydantic import BaseModel
from typing import Optional


class ConfigStorageMemoryBackup(BaseModel):
    """
    {
        "dir": "/path/to/backup",
        "patterns": ["path/to/*.jpg"]
    }
    """

    dir: Optional[str]
    patterns: Optional[list[str]]
