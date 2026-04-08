from pydantic import BaseModel
from typing import Optional, List


class ConfigStorageCors(BaseModel):
    """
    {
        "origins": ["*"]
    }
    """

    origins: list[str] | None = None
