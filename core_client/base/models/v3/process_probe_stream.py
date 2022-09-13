from pydantic import BaseModel


class ProcessProbeStream(BaseModel):
    """
    {
        "bitrate_kbps": 0,
        "channels": 0,
        "codec": "string",
        "coder": "string",
        "duration_sec": 0,
        "format": "string",
        "fps": 0,
        "height": 0,
        "index": 0,
        "language": "string",
        "layout": "string",
        "pix_fmt": "string",
        "sampling_hz": 0,
        "stream": 0,
        "type": "string",
        "url": "string",
        "width": 0
    }
    """

    bitrate_kbps: int
    channels: int
    codec: str
    coder: str
    duration_sec: int
    format: str
    fps: int
    height: int
    index: int
    language: str
    layout: str
    pix_fmt: str
    sampling_hz: int
    stream: int
    type: str
    url: str
    width: int
