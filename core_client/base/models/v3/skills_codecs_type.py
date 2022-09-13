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

    decoders: Union[None, List[str]]
    encoders: Union[None, List[str]]
    id: str
    name: str
