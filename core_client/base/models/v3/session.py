from pydantic import BaseModel
from typing import Optional

from . import SessionCollector


class Session(BaseModel):
    """
    {
        "ffmpeg": SessionCollector,
        "hls": SessionCollector,
        "hlsingress": SessionCollector,
        "http": SessionCollector,
        "rtmp": SessionCollector,
        "srt": SessionCollector
    }
    """

    ffmpeg: SessionCollector | None = None
    hls: SessionCollector | None = None
    hlsingress: SessionCollector | None = None
    http: SessionCollector | None = None
    rtmp: SessionCollector | None = None
    srt: SessionCollector | None = None
