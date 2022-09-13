from pydantic import BaseModel
from typing import List

from . import SkillsFfmpegLibrarie


class SkillsFfmpeg(BaseModel):
    """
    {
        "compiler": "string",
        "configuration": "string",
        "libraries": [SkillsFfmpegLibrarie],
        "version": "string"
    }
    """

    compiler: str
    configuration: str
    libraries: List[SkillsFfmpegLibrarie]
    version: str
