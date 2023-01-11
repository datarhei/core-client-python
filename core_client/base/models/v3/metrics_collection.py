from pydantic import BaseModel


class MetricsCollection(BaseModel):
    name: str
    description: str
    labels: list[str]
