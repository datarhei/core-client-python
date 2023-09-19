from pydantic import BaseModel
from typing import List, Optional

from . import IamUserPolicyType

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
    +  {
        "type": ["fs", "srt", "rtmp"]
    }
    """

    actions: Optional[List[str]]
    domain: Optional[str]
    name: Optional[str]
    resource: Optional[str]
    type: Optional[List[IamUserPolicyType]]
