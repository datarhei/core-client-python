from pydantic import BaseModel


class Filesystem(BaseModel):
    """
    {
        "name": "disk",
        "type": "diskfs",
        "mount": "/"
    }
    """

    name: str
    type: str
    mount: str
