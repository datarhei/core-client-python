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

    basic: Optional[List[str]] = None
    session: Optional[List[str]] = None
    token: Optional[List[str]] = None
