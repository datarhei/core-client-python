from pydantic_collections import BaseCollectionModel

from . import ClusterDbLock


class ClusterDbLockList(BaseCollectionModel[ClusterDbLock]):
    pass
