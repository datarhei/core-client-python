from pydantic import RootModel

from . import ConfigStorageS3

# JSON array of ConfigStorageS3.
ConfigStorageS3List = RootModel[list[ConfigStorageS3]]
