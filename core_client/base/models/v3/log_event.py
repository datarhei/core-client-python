from pydantic import BaseModel


class LogEvent(BaseModel):
    """
    {
        "caller": "string",
        "core_id": "string",
        "data": {},
        "event": "string",
        "level": int,
        "message": "string",
        "ts": int
    }
    """

    caller: str | None = None
    core_id: str | None = None
    data: dict | None = None
    event: str | None = None
    level: int | None = None
    message: str | None = None
    ts: int | None = None
