from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class RoadUserTypes(str, Enum):
    """The road user types:
      - Vehicle: Vehicles with a metal box. Example: Car, Truck, Bus, etc.
      - VulnerableRoadUser: Road users without protective housing. Example: Pedestrian, Cyclist, Motorcyclist, etc."""

    VULNERABLE_ROAD_USER = "VulnerableRoadUser"
    VEHICLE = "Vehicle"

    __str__ = str.__str__


RoadUserTypesOrStr: TypeAlias = Annotated[RoadUserTypes | str, open_enum_validator(RoadUserTypes)]
