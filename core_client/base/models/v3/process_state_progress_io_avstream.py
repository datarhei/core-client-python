from pydantic import BaseModel

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
    duplicating: bool
    gop: str
