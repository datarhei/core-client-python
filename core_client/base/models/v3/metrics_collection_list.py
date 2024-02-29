from pydantic import RootModel

from . import MetricsCollection


MetricsCollectionList = RootModel[list[MetricsCollection]]
