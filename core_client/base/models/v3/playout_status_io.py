from pydantic import BaseModel


class PlayoutStatusIO(BaseModel):
    """
    {
        "packet": int,
        "size_kb": int,
        "state": "string",
        "time": int
    }
    """

    packet: int | None = None
    size_kb: int | None = None
    state: str | None = None
    time: int | None = None
