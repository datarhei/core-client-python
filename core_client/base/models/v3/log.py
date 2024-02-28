from pydantic import BaseModel, RootModel
from typing import List, Union


class Log(BaseModel):
    RootModel: List[Union[str, dict]]
