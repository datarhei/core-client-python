from pydantic import BaseModel
from typing import Optional, List


class ConfigApiAccessRules(BaseModel):
    """
    {
        "allow": [],
        "block": []
    }
    """

    allow: Optional[List[str]]
    block: Optional[List[str]]
