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

    ffmpeg: Optional[SessionCollector]
    hls: Optional[SessionCollector]
    hlsingress: Optional[SessionCollector]
    http: Optional[SessionCollector]
    rtmp: Optional[SessionCollector]
    srt: Optional[SessionCollector]
