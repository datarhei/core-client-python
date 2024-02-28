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

    input: Optional[ConfigFfmpegAccessRules] = None
    output: Optional[ConfigFfmpegAccessRules] = None
