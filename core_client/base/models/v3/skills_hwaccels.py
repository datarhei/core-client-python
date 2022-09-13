from pydantic import BaseModel


class SkillsHwaccels(BaseModel):
    """
    {
        "id": "string",
        "name": "string"
    }
    """

    id: str
    name: str
