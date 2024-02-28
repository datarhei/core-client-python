from pydantic import BaseModel, RootModel

from . import MetricsCollection


class MetricsCollectionList(BaseModel):
    RootModel: list[MetricsCollection]
