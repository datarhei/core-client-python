from typing import Optional
from pydantic import BaseModel


class ProcessConfigIOCleanup(BaseModel):
    """
    {
        "max_file_age_seconds": 0,
        "max_files": 0,
        "pattern": "",
        "purge_on_delete": true
    }
    """

    max_file_age_seconds: Optional[int] = 0
    max_files: Optional[int] = 0
    pattern: str
    purge_on_delete: bool = True
