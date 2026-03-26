from pydantic import BaseModel
from typing import List, Optional


class IamUserAuthServices(BaseModel):
    """
    {
        "basic": [
            "string"
        ],
        "session": [
            "string"
        ],
        "token": [
            "string"
        ]
    }
    """

    basic: list[str] | None = None
    session: list[str] | None = None
    token: list[str] | None = None
