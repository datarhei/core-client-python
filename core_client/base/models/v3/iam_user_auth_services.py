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

    basic: Optional[List[str]]
    session: Optional[List[str]]
    token: Optional[List[str]]
