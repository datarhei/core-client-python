from pydantic import BaseModel
from typing import List, Optional

from . import SessionCollectorActiveSession


class SessionActive(BaseModel):
    """
    {
        "ffmpeg": [SessionCollectorActiveSession],
        "hls": [SessionCollectorActiveSession],
        "hlsingress": [SessionCollectorActiveSession],
        "http": [SessionCollectorActiveSession],
        "rtmp": [SessionCollectorActiveSession],
        "srt": [SessionCollectorActiveSession]
    }
    """

    ffmpeg: list[SessionCollectorActiveSession] | None = None
    hls: list[SessionCollectorActiveSession] | None = None
    hlsingress: list[SessionCollectorActiveSession] | None = None
    http: list[SessionCollectorActiveSession] | None = None
    rtmp: list[SessionCollectorActiveSession] | None = None
    srt: list[SessionCollectorActiveSession] | None = None
