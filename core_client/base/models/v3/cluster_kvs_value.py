from pydantic import BaseModel


class ClusterKVSValue(BaseModel):
    """
    {
        "updated_at": "string",
        "value": "string"
    }
    """

    updated_at: str | None = None
    value: str | None = None
