from pydantic import BaseModel
from typing import Optional, List


class ConfigFfmpegAccessRules(BaseModel):
    """
    {
        "allow": [],
        "block": []
    }
    """

    allow: Optional[List[str]]
    block: Optional[List[str]]
