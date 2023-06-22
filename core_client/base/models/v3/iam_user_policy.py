from pydantic import BaseModel
from typing import List, Optional


class IamUserPolicy(BaseModel):
    """
    {
        "actions": [
            "string"
        ],
        "domain": "string",
        "name": "string",
        "resource": "string"
    }
    """

    actions: Optional[List[str]]
    domain: Optional[str]
    name: Optional[str]
    resource: Optional[str]
