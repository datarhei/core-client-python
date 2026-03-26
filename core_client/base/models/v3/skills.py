from pydantic import BaseModel
from typing import List

from . import (
    SkillsCodecs,
    SkillsDevices,
    SkillsFfmpeg,
    SkillsFilter,
    SkillsFormat,
    SkillsHwaccels,
    SkillsProtocol,
)


class Skills(BaseModel):
    """
    {
        "codecs": SkillsCodecs,
        "devices": SkillsDevices,
        "ffmpeg": SkillsFfmpeg,
        "filter": [SkillsFilter],
        "formats": SkillsFormat,
        "hwaccels": [SkillsHwaccels],
        "protocols": SkillsProtocol
    }
    """

    codecs: SkillsCodecs
    devices: SkillsDevices
    ffmpeg: SkillsFfmpeg
    filter: list[SkillsFilter]
    formats: SkillsFormat
    hwaccels: list[SkillsHwaccels]
    protocols: SkillsProtocol
