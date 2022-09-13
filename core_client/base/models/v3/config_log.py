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

    level: Optional[str]
    topics: Optional[List[str]]
    max_lines: Optional[int]
