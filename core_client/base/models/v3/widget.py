from pydantic import BaseModel


class Widget(BaseModel):
    """
    {
        "current_sessions": 0,
        "total_sessions": 0,
        "uptime": 0
    }
    """

    current_sessions: int
    total_sessions: int
    uptime: int
