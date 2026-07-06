from pydantic import RootModel

from . import ClusterDbLock

# JSON array of ClusterDbLock.
ClusterDbLockList = RootModel[list[ClusterDbLock]]
