from typing import List, Optional
from pydantic import BaseModel

from . import (
    ProcessStateProgress,
    ProcessStateExec,
    ProcessStateOrder,
    ProcessStateResources,
)


class ProcessState(BaseModel):
    """
    {
        "command": [
            "-err_detect",
            "ignore_err",
            "-i",
            "http://127.0.0.1:8080/memfs/abc.m3u8",
            "-vframes",
            "1",
            "-f",
            "image2",
            "-update",
            "1",
            "http://127.0.0.1:8080/memfs/abc.jpg"
        ],
        "cpu_usage": 0,
        "exec": "finished",
        "last_logline": "      cpb: bitrate max/min/avg: 0/0/200000 buffer size: 0 vbv_delay: N/A",
        "memory_bytes": 0,
        "order": "start",
        "progress": ProcessStateProgress,
        "reconnect_seconds": 11,
        "runtime_seconds": 48
    }
    """

    """
    + {
        "resources": ProcessStateResources
    }
    """

    command: List[str]
    cpu_usage: float
    exec: ProcessStateExec
    last_logline: str
    memory_bytes: float
    order: ProcessStateOrder
    progress: Optional[ProcessStateProgress]
    reconnect_seconds: int
    runtime_seconds: int
    resources: Optional[ProcessStateResources]

    class Config:
        use_enum_values = True
