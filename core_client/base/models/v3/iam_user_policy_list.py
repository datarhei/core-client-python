from pydantic_collections import BaseCollectionModel

from . import IamUserPolicy


class IamUserPolicyList(BaseCollectionModel[IamUserPolicy]):
    """
    [IamUserPolicy]
    """

    pass
