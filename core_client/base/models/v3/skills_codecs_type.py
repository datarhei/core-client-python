from pydantic import BaseModel
from typing import Union, List


class SkillsCodecsType(BaseModel):
    """
    {
        "decoders": [
            "string"
        ],
        "encoders": [
            "string"
        ],
        "id": "string",
        "name": "string"
    }
    """

    decoders: None | list[str]
    encoders: None | list[str]
    id: str
    name: str
