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

    profiling: bool | None = None
    force_gc: int | None = None
    memory_limit_mbytes: int | None = None
    auto_max_procs: bool | None = None
