from pydantic import RootModel

from . import ClusterNode

# JSON array of ClusterNode.
ClusterNodeList = RootModel[list[ClusterNode]]
