from pydantic import BaseModel
from typing import List

from . import SkillsCodecsType


class SkillsCodecs(BaseModel):
    """
    {
        "audio": [SkillsCodecsType],
        "subtitle": [SkillsCodecsType],
        "video": [SkillsCodecsType]
    }
    """

    audio: List[SkillsCodecsType]
    subtitle: List[SkillsCodecsType]
    video: List[SkillsCodecsType]
