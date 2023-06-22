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

    level: Optional[str]
    topics: Optional[List[str]]
    max_lines: Optional[int]
    max_minimal_history: Optional[int]
