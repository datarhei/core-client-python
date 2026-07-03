from pydantic import BaseModel

from . import ClusterDeploymentsProcess


class ClusterDeployments(BaseModel):
    """
    {
        "process": [ClusterDeploymentsProcess]
    }
    """

    process: list[ClusterDeploymentsProcess] | None = None
