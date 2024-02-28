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

    binary: Optional[str] = None
    max_processes: Optional[int] = None
    access: Optional[ConfigFfmpegAccess] = None
    log: Optional[ConfigFfmpegLog] = None
