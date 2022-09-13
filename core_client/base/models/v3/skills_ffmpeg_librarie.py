from pydantic import BaseModel


class SkillsFfmpegLibrarie(BaseModel):
    """
    {
        "compiled": "string",
        "linked": "string",
        "name": "string"
    }
    """

    compiled: str
    linked: str
    name: str
