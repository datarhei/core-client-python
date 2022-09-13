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

    input: Optional[ConfigFfmpegAccessRules]
    output: Optional[ConfigFfmpegAccessRules]
