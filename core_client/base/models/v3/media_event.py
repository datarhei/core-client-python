from pydantic import BaseModel


class MediaEvent(BaseModel):
    """
    {
        "action": "string",
        "name": "string",
        "names": ["string"],
        "ts": int
    }
    """

    action: str | None = None
    name: str | None = None
    names: list[str] | None = None
    ts: int | None = None
