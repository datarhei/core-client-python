from pydantic import BaseModel
from typing import Optional


class ConfigDebug(BaseModel):
    """
    {
        "profiling": False,
        "force_gc": 0
    }
    """

    """
    + {
        "auto_max_procs": bool,
    }
    """

    profiling: Optional[bool]
    force_gc: Optional[int]
    memory_limit_mbytes: Optional[int]
    auto_max_procs: Optional[bool]
