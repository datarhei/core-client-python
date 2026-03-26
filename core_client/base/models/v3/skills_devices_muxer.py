from pydantic import BaseModel
from typing import List

from . import SkillsDevicesMuxerDevice


class SkillsDevicesMuxer(BaseModel):
    """
    {
        "devices": [SkillsDevicesMuxerDevice],
        "id": "string",
        "name": "string"
    }
    """

    devices: list[SkillsDevicesMuxerDevice]
    id: str
    name: str
