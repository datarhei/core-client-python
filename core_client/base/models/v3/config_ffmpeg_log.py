from pydantic import BaseModel
from typing import Optional


class ConfigFfmpegLog(BaseModel):
    """
    {
        "max_lines": 50,
        "max_history": 3
    }
    """

    """new in vod branch
    {
        "max_minimal_history": int
    }
    """

    max_lines: Optional[int]
    max_history: Optional[int]
    max_minimal_history: Optional[int]
