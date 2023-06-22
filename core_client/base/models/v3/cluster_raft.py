from pydantic import BaseModel
from typing import List

from . import ClusterRaftServer, ClusterRaftStats


class ClusterRaft(BaseModel):
    """
    {
        "server": [
            {
                "address": "string",
                "id": "string",
                "leader": true,
                "voter": true
            }
        ],
        "stats": {
            "last_contact_ms": 0,
            "num_peers": 0,
            "state": "string"
        }
    }
    """

    server: List[ClusterRaftServer]
    stats: ClusterRaftStats
