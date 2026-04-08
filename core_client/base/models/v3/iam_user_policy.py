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

    actions: list[str] | None = None
    domain: str | None = None
    name: str | None = None
    resource: str | None = None
    types: list[IamUserPolicyTypes] | None = None

    class ConfigDict:
        use_enum_values = True
