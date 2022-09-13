from pydantic import BaseModel
from typing import Optional

from . import ConfigFfmpegAccess, ConfigFfmpegLog


class ConfigFfmpeg(BaseModel):
    """
    {
        "binary": "ffmpeg",
        "max_processes": 0,
        "access": ConfigFfmpegAccess,
        "log": ConfigFfmpegLog
    }
    """

    binary: Optional[str]
    max_processes: Optional[int]
    access: Optional[ConfigFfmpegAccess]
    log: Optional[ConfigFfmpegLog]
