from pydantic import BaseModel, Field


class ProcessStateProgressMappingMap(BaseModel):
    """
     {
        "input": 1,
        "output": -1,
        "index": 0,
        "name": "graph_0_in_1_0",
        "copy": false
    }
    """

    input: int
    output: int
    index: int
    name: str
    alias_copy: bool = Field(alias="copy")
    
    class ConfigDict:
        populate_by_name = False
    @property
    def copy(self):
        return self.alias_copy
    @copy.setter
    def copy(self, value):
        self.alias_copy = value
