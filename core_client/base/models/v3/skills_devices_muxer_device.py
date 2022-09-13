from pydantic import BaseModel


class SkillsDevicesMuxerDevice(BaseModel):
    """
    {
        "extra": "string",
        "id": "string",
        "media": "string",
        "name": "string"
    }
    """

    extra: str
    id: str
    media: str
    name: str
