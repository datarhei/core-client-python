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

    level: Optional[str] = None
    topics: Optional[List[str]] = None
    max_lines: Optional[int] = None
    max_minimal_history: Optional[int] = None
