from pydantic import BaseModel
from typing import Optional

from . import ConfigFfmpegAccessRules


class ConfigFfmpegAccess(BaseModel):
    """
    {
        "input": ConfigFfmpegAccessRules,
        "output": ConfigFfmpegAccessRules
    }
    """

    input: ConfigFfmpegAccessRules | None = None
    output: ConfigFfmpegAccessRules | None = None
