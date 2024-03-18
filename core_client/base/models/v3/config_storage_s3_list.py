from pydantic import BaseModel, RootModel

from . import ConfigStorageS3


class ConfigStorageS3List(BaseModel):
    """
    [ConfigStorageS3]
    """

    RootModel: ConfigStorageS3
