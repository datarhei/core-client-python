from pydantic_collections import BaseCollectionModel

from . import Process


class ProcessList(BaseCollectionModel[Process]):
    pass
