from pydantic import RootModel
from typing import List, Union


Log = RootModel[list[Union[str, dict]]]
