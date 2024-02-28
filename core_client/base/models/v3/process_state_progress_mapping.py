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

    graphs: List[ProcessStateProgressMappingGraph]
    mapping: List[ProcessStateProgressMappingMap]
