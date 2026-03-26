from pydantic import BaseModel
from typing import Optional


class ConfigClusterDebug(BaseModel):
    """
    {
        "disable_ffmpeg_check": true,
    }
    """

    disable_ffmpeg_check: bool | None = None
