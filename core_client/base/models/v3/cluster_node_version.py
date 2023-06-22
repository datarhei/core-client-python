from pydantic import BaseModel


class ClusterNodeVersion(BaseModel):
    """
    {
        "arch": "string",
        "build_date": "string",
        "compiler": "string",
        "number": "string",
        "repository_branch": "string",
        "repository_commit": "string"
    }
    """

    arch: str
    build_date: str
    compiler: str
    number: str
    repository_branch: str
    repository_commit: str
