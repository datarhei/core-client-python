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
        "duplicating": false,
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
    gop: str
    time: Optional[int]
