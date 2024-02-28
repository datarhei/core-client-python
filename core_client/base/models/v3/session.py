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

    ffmpeg: Optional[SessionCollector] = None
    hls: Optional[SessionCollector] = None
    hlsingress: Optional[SessionCollector] = None
    http: Optional[SessionCollector] = None
    rtmp: Optional[SessionCollector] = None
    srt: Optional[SessionCollector] = None
