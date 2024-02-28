from pydantic import BaseModel
from typing import Optional

from . import ProcessStateProgressIOAvstreamIO


class ProcessStateProgressIOAvstream(BaseModel):
    """
    {
        "input": {ProcessStateProgressIOAvstreamIO},
        "output": {ProcessStateProgressIOAvstreamIO},
        "aqueue": 0,
        "queue": 124,
        "dup": 46212,
        "drop": 0,
        "enc": 154,
        "looping": false,
        + "looping_runtime": 0,
        "duplicating": false,
        + "mode": "live",
        "gop": "none"
        + "time": 0,
    }
    """

    input: ProcessStateProgressIOAvstreamIO
    output: ProcessStateProgressIOAvstreamIO
    aqueue: int
    queue: float
    dup: int
    drop: int
    enc: int
    looping: bool
    looping_runtime: int
    duplicating: bool
    mode: Optional[str] = None
    gop: str
    time: Optional[int] = None
