from pydantic import BaseModel
from typing import List

from . import SkillsDevicesMuxer


class SkillsDevices(BaseModel):
    """
    {
        "demuxers": [SkillsDevicesMuxer],
        "muxers": [SkillsDevicesMuxer ]
    }
    """

    demuxers: List[SkillsDevicesMuxer]
    muxers: List[SkillsDevicesMuxer]
