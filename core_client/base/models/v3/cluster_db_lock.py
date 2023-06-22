from pydantic import BaseModel


class ClusterDbLock(BaseModel):
    """
    {
        "name": "string",
        "valid_until": "string"
    }
    """

    name: str
    valid_until: str
