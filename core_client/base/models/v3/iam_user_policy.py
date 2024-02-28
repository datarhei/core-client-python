from pydantic import BaseModel
from typing import List, Optional

from . import IamUserPolicyTypes

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

    actions: Optional[List[str]] = None
    domain: Optional[str] = None
    name: Optional[str] = None
    resource: Optional[str] = None
    types: Optional[List[IamUserPolicyTypes]] = None

    class ConfigDict:
        use_enum_values = True