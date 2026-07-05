from pydantic import BaseModel


class ClusterStoreNode(BaseModel):
    """
    {
        "id": "string",
        "state": "string",
        "updated_at": "string"
    }
    """

    id: str | None = None
    state: str | None = None
    updated_at: str | None = None
