from pydantic_collections import BaseCollectionModel

from . import ClusterNode


class ClusterNodeList(BaseCollectionModel[ClusterNode]):
    pass
