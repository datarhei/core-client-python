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

    max_lines: int | None = None
    max_history: int | None = None
    max_minimal_history: int | None = None
