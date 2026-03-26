from pydantic import BaseModel
from typing import Optional

from . import ClusterReallocationNodeProcess


class ClusterReallocationNode(BaseModel):
    """
    [
        {
            "target_node_id": "abc",
            "process_ids": [
                ClusterReallocationProcess,
                ...
            ]
        }
    ]
    """

    target_node_id: str | None = ""
    process_ids: list[ClusterReallocationNodeProcess]
