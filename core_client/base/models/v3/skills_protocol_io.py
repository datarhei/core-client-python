from pydantic import BaseModel


class SkillsProtocolIO(BaseModel):
    """
    {
        "id": "string",
        "name": "string"
    }
    """

    id: str
    name: str
