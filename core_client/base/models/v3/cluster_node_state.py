from pydantic import BaseModel
from enum import Enum

from . import ClusterNodeStateValue



class ClusterNodeState(BaseModel):
    """
    {
        "state": "online",
    }
    """

    state: ClusterNodeStateValue
