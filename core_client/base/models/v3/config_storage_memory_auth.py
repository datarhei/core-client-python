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

    enable: bool | None = None
    username: str | None = None
    password: str | None = None
