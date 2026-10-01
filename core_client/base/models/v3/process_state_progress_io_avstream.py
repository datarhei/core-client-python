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
        + "codec": "h264",
        + "profile": 100,
        + "level": 40,
        + "pix_fmt": "yuv420p",
        + "width": 1920,
        + "height": 1080,
        + "sampling_hz": 48000,
        + "layout": "stereo",
        + "channels": 2,
        + "sample_fmt": "fltp"
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
    mode: str | None = None
    gop: str
    time: int | None = None
    codec: str | None = None
    profile: int | None = None
    level: int | None = None
    pix_fmt: str | None = None
    width: int | None = None
    height: int | None = None
    sampling_hz: int | None = None
    layout: str | None = None
    channels: int | None = None
    sample_fmt: str | None = None
