from typing import List
from enum import Enum
from pydantic import BaseModel


class BikeState(str, Enum):
    FREE = "FREE"
    RESERVED = "RESERVED"
    BROKEN = "BROKEN"


class Bike(BaseModel):
    id: str
    name: str = None
    state: BikeState = None


class Station(BaseModel):
    id: str
    name: str
    bikes: List[Bike]
