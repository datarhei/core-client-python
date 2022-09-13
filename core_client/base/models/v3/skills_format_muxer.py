from pydantic import BaseModel


class SkillsFormatMuxer(BaseModel):
    """
    {
        "id": "string",
        "name": "string"
    }
    """

    id: str
    name: str
