from pydantic import BaseModel, RootModel

from . import Process


class ProcessList(BaseModel):
    RootModel: Process
