from pydantic_collections import BaseCollectionModel

from . import Srt


class SrtList(BaseCollectionModel[Srt]):
    pass
