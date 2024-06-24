from pydantic import BaseModel, RootModel

from . import ClusterReallocationNode


class ClusterReallocation(BaseModel):
    RootModel: ClusterReallocationNode
