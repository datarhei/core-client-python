from pydantic import RootModel
from typing import List, Union


Log = RootModel[List[Union[str, dict]]]
