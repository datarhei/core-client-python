from typing import Optional
from pydantic import BaseModel, model_validator

from . import ProcessStateProgressIOAvstream, ProcessStateProgressIOFramerate, ProcessStateProgressIOTee


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

    """new in vod branch
    {
        "tee_outputs": float,
    }
    """

    address: str
    avstream: ProcessStateProgressIOAvstream | None = None
    bitrate_kbit: float
    channels: int | None = None
    codec: str
    coder: str
    format: str
    fps: float
    frame: float
    framerate: ProcessStateProgressIOFramerate | None = None
    keyframe: float | None = None
    extradata_size_bytes: float | None = None
    height: int | None = None
    id: str
    index: int
    layout: str | None = None
    packet: float
    pix_fmt: str | None = None
    pps: float
    q: float | None = None
    sampling_hz: float | None = None
    size_kb: float
    stream: int
    type: str
    width: int | None = None
    gop: float | None = None
    drop: int | None = None
    tee: list[ProcessStateProgressIOTee] | None = None

    @model_validator(mode="before")
    def remove_empty(cls, values):
        fields = list(values.keys())
        for field in fields:
            if values[field] == {}:
                values.pop(field)
        return values
