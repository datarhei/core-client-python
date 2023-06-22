from pydantic import BaseModel
from typing import Optional


class ConfigStorageS3Auth(BaseModel):
    """
    {
        "enable": True,
        "username": "admin",
        "password": "5w4DMJNTypt4Rv0YRN"
    }
    """

    enable: Optional[bool]
    username: Optional[str]
    password: Optional[str]
