from pydantic_collections import BaseCollectionModel

from . import IamUser


class IamUserList(BaseCollectionModel[IamUser]):
    """
    [IamUser]
    """

    pass
