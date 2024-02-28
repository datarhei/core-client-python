from typing import List
from pydantic import BaseModel


class ProcessStateProgressMappingGraph(BaseModel):
    """
    {
        "index": 0,
        "name": "Parsed_anull_0",
        "filter": "anull",
        "dst_name": "auto_aresample_0",
        "dst_filter": "aresample",
        "inpad": "default",
        "outpad": "default",
        "timebase": "1/44100",
        "type": "audio",
        "format": "u8",
        "sampling": 44100,
        "layout": "mono",
        "width": 0,
        "height": 0
    }
    """

    index: int
    name: str
    filter: str
    dst_name: str
    dst_filter: str
    inpad: str
    outpad: str
    timebase: str
    type: str
    format: str
    sampling: int
    layout: str
    width: int
    height: int
