from pydantic import BaseModel
from typing import Optional, List


class ConfigStorageCors(BaseModel):
    """
    {
        "origins": ["*"]
    }
    """

    origins: Optional[List[str]] = None
