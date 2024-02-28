from typing import Optional
from pydantic import BaseModel, model_validator

from . import ProcessStateProgressIOAvstream, ProcessStateProgressIOFramerate


class ProcessStateProgressIO(BaseModel):
    """
    {
        "address": "http://127.0.0.1:8080/memfs/abc.m3u8",
        "avstream": null,
        "bitrate_kbit": 1994.933,
        "codec": "h264",
        "coder": "h264",
        "format": "hls",
        "fps": 24.9,
        "frame": 2195923,
        "id": "input_0",
        "index": 0,
        "packet": 2195923,
        "pps": 24.9,
        "q": 0,
        "size_kb": 21973597,
        "stream": 0,
        "type": "video",
        [--- type: video ---]
        "height": 720,
        "pix_fmt": "yuv420p",
        "width": 1280,
        [-------------------]
        [--- type: audio ---]
        "channels": 2,
        "layout": 2,
        "sampling_hz": 44100,
        [-------------------]
    }
    """

    """new in vod branch
    {
        "keyframe": float,
        "extradata_size_bytes": ProcessStateExec,
        "framerate": ProcessStateProgressIOFramerate,
    }
    """

    address: str
    avstream: Optional[ProcessStateProgressIOAvstream] = None
    bitrate_kbit: float
    channels: Optional[int] = None
    codec: str
    coder: str
    format: str
    fps: float
    frame: float
    framerate: Optional[ProcessStateProgressIOFramerate] = None
    keyframe: Optional[float] = None
    extradata_size_bytes: Optional[float] = None
    height: Optional[int] = None
    id: str
    index: int
    layout: Optional[str] = None
    packet: float
    pix_fmt: Optional[str] = None
    pps: float
    q: Optional[float] = None
    sampling_hz: Optional[float] = None
    size_kb: float
    stream: int
    type: str
    width: Optional[int] = None

    @model_validator(mode="before")
    def remove_empty(cls, values):
        fields = list(values.keys())
        for field in fields:
            if values[field] == {}:
                values.pop(field)
        return values
