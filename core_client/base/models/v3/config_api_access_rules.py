from pydantic import BaseModel
from typing import Optional, List


class ConfigApiAccessRules(BaseModel):
    """
    {
        "allow": [],
        "block": []
    }
    """

    allow: list[str] | None = None
    block: list[str] | None = None
