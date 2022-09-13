from pydantic import BaseModel


class Rtmp(BaseModel):
    """
    {
        "name": "string"
    }
    """

    name: str
