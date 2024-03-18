from pydantic import BaseModel, RootModel

from . import ClusterNode


class ClusterNodeList(BaseModel):
    RootModel: list[ClusterNode]
