from pydantic import BaseModel
from typing import Optional, List


class ConfigFfmpegAccessRules(BaseModel):
    """
    {
        "allow": [],
        "block": []
    }
    """

    allow: Optional[List[str]] = None
    block: Optional[List[str]] = None
