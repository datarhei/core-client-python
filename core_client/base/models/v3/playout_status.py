from typing import Any

from pydantic import BaseModel

from . import PlayoutStatusIO, PlayoutStatusSwap


class PlayoutStatus(BaseModel):
    """
    {
        "aqueue": int,
        "debug": {},
        "drop": int,
        "dup": int,
        "duplicating": bool,
        "enc": int,
        "gop": "string",
        "id": "string",
        "input": PlayoutStatusIO,
        "looping": bool,
        "output": PlayoutStatusIO,
        "queue": int,
        "stream": int,
        "swap": PlayoutStatusSwap,
        "url": "string"
    }
    """

    aqueue: int | None = None
    debug: Any = None
    drop: int | None = None
    dup: int | None = None
    duplicating: bool | None = None
    enc: int | None = None
    gop: str | None = None
    id: str | None = None
    input: PlayoutStatusIO | None = None
    looping: bool | None = None
    output: PlayoutStatusIO | None = None
    queue: int | None = None
    stream: int | None = None
    swap: PlayoutStatusSwap | None = None
    url: str | None = None
