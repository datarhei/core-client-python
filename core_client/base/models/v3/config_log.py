from pydantic import BaseModel
from typing import Optional, List


class ConfigLog(BaseModel):
    """
    {
        "level": "info",
        "topics": [],
        "max_lines": 1000
    }
    """

    """
    + {
        "max_minimal_history": int,
    }
    """

    level: str | None = None
    topics: list[str] | None = None
    max_lines: int | None = None
    max_minimal_history: int | None = None
