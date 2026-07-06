from pydantic import RootModel

from . import ClusterReallocationNode

# The reallocation body is a JSON array of nodes:
# [{"target_node_id": "abc", "process_ids": [{"id": "p1", "domain": "d"}]}]
ClusterReallocation = RootModel[list[ClusterReallocationNode]]
