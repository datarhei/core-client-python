from typing import List
from pydantic import BaseModel

from . import ProcessStateProgressMappingGraph, ProcessStateProgressMappingMap


class ProcessStateProgressMapping(BaseModel):
    """
    {
        "graphs": [],
        "mapping": []
    }
    """

    graphs: list[dict]
    mapping: list[dict]
