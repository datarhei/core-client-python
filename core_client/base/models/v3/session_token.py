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

    match: str = "/**"
    ttl_sec: int = 3600
    extras: Optional[Dict[str, Dict]] = None
    remote: Optional[List[str]] = None
    token: Optional[str] = None
