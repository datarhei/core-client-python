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

    ffmpeg: Optional[List[SessionCollectorActiveSession]] = None
    hls: Optional[List[SessionCollectorActiveSession]] = None
    hlsingress: Optional[List[SessionCollectorActiveSession]] = None
    http: Optional[List[SessionCollectorActiveSession]] = None
    rtmp: Optional[List[SessionCollectorActiveSession]] = None
    srt: Optional[List[SessionCollectorActiveSession]] = None
