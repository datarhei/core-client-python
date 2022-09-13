from pydantic import BaseModel


class SkillsFilter(BaseModel):
    """
    {
        "id": "string",
        "name": "string"
    }
    """

    id: str
    name: str
