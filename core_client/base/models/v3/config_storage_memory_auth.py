from pydantic import BaseModel
from typing import Optional


class ConfigStorageMemoryAuth(BaseModel):
    """
    {
        "enable": True,
        "username": "admin",
        "password": "5w4DMJNTypt4Rv0YRN"
    }
    """

    enable: Optional[bool] = None
    username: Optional[str] = None
    password: Optional[str] = None
