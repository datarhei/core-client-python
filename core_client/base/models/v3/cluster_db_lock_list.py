from pydantic import BaseModel, RootModel

from . import ClusterDbLock


class ClusterDbLockList(BaseModel):
    RootModel: ClusterDbLock
