from pydantic import BaseModel
from typing import List

from . import SkillsFormatMuxer


class SkillsFormat(BaseModel):
    """
    {
        "demuxers": [SkillsFormatMuxer],
        "muxers": [SkillsFormatMuxer]
    }
    """

    demuxers: list[SkillsFormatMuxer]
    muxers: list[SkillsFormatMuxer]
