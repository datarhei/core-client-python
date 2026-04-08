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

    binary: str | None = None
    max_processes: int | None = None
    access: ConfigFfmpegAccess | None = None
    log: ConfigFfmpegLog | None = None
