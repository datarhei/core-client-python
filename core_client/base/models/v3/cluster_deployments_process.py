from enum import Enum

from pydantic import BaseModel


class ClusterDeploymentsProcessAction(str, Enum):
    delete = "delete"
    update = "update"
    add = "add"
    order = "order"
    relocate = "relocate"


class ClusterDeploymentsProcess(BaseModel):
    """
    {
        "action": "delete" | "update" | "add" | "order" | "relocate",
        "domain": "string",
        "error": "string",
        "id": "string",
        "node_id": "string",
        "order": "string",
        "updated_at": int
    }
    """

    action: ClusterDeploymentsProcessAction
    domain: str | None = None
    error: str | None = None
    id: str | None = None
    node_id: str | None = None
    order: str | None = None
    updated_at: int | None = None
