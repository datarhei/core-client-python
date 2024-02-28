from pydantic import BaseModel
from typing import Optional, Dict, List


class SessionToken(BaseModel):
    """
    {
        "extra": {
            "additionalProp1": {}
        },
        "match": "string",
        "remote": [
            "string"
        ],
        "token": "string"
    }
    """

    extras: Optional[Dict[str, Dict]] = None
    match: Optional[str] = None
    remote: Optional[List[str]] = None
    token: Optional[str] = None
