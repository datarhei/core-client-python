from pydantic import BaseModel

from . import MetricsCollection


class MetricsCollectionList(BaseModel):
    __root__: list[MetricsCollection]
