from pydantic import BaseModel


class LogEventFilter(BaseModel):
    """
    {
        "caller": "string",
        "core_id": "string",
        "data": {"string": "string"},
        "event": "string",
        "level": "string",
        "message": "string"
    }
    """

    caller: str | None = None
    core_id: str | None = None
    data: dict[str, str] | None = None
    event: str | None = None
    level: str | None = None
    message: str | None = None
