from pydantic import BaseModel
from typing import List

from . import SkillsProtocolIO


class SkillsProtocol(BaseModel):
    """
    {
        "input": [SkillsProtocolIO],
        "output": [SkillsProtocolIO]
    }
    """

    input: List[SkillsProtocolIO]
    output: List[SkillsProtocolIO]
