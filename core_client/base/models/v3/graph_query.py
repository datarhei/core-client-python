from pydantic import BaseModel


class GraphQuery(BaseModel):
    """
    {
        "query": "string",
        "variables": {}
    }
    """

    query: str | None = None
    variables: dict | None = None
