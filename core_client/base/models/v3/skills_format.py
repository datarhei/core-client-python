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

    demuxers: List[SkillsFormatMuxer]
    muxers: List[SkillsFormatMuxer]
