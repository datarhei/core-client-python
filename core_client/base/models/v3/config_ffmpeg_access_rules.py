from pydantic import BaseModel
from typing import Optional, List


class ConfigFfmpegAccessRules(BaseModel):
    """
    {
        "allow": [],
        "block": []
    }
    """

    allow: list[str] | None = None
    block: list[str] | None = None
