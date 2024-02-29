from pydantic import BaseModel, Field
from typing import Dict, Any, List, Optional


class Control(BaseModel):
    name: Optional[str] = None
    type: str
    params: Dict[str, Any]


class Step(BaseModel):
    name: str
    type: str
    input: str = Field(default="one")
    output: str = Field(default="one")
    params: Dict[str, Any]
    version: float
    controls: List[Control] = []


class Pipeline(BaseModel):
    id: str
    name: str
    description: str
    steps: List[Step] = []
    controls: Any
    params: Dict[str, Any]

