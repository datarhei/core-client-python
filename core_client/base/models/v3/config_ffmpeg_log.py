from pydantic import BaseModel
from typing import Optional


class ConfigFfmpegLog(BaseModel):
    """
    {
        "max_lines": 50,
        "max_history": 3
    }
    """

    max_lines: Optional[int]
    max_history: Optional[int]
