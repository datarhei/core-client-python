from pydantic import BaseModel
from typing import Optional, List


class ConfigApiAccessRules(BaseModel):
    """
    {
        "allow": [],
        "block": []
    }
    """

    allow: Optional[List[str]] = None
    block: Optional[List[str]] = None
