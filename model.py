from typing import List
from enum import Enum
from pydantic import BaseModel


class BikeState(str, Enum):
    FREE = "free"
    RESERVED = "reserved"
    BROKEN = "broken"


class BikeType(str, Enum):
    NORMAL = "Normal Bike"
    FAST = "Fast Bike"


class Bike(BaseModel):
    id: str
    type: BikeType = None
    stationed_at: str = None
    state: BikeState = None
    battery: int = None


class Station(BaseModel):
    id: str
    name: str
    bikes: List[str]
