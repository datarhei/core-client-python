from pydantic import RootModel

from . import IamUserPolicy

# JSON array of IamUserPolicy.
IamUserPolicyList = RootModel[list[IamUserPolicy]]
