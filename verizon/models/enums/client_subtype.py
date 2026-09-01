from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ClientSubtype(str, Enum):
    """The subtype or subgroup of the client type. This further specifies the client type. For example it will specify
    if the client is a passenger car or a truck. See the ClientType description for the supported Subtypes for each
    client type."""

    PASSENGER_CAR = "PassengerCar"
    TRUCK = "Truck"
    BUS = "Bus"
    EMERGENCY_VEHICLE = "EmergencyVehicle"
    SCHOOL_BUS = "SchoolBus"
    MAINTENANCE_VEHICLE = "MaintenanceVehicle"
    PEDESTRIAN = "Pedestrian"
    BICYCLE = "Bicycle"
    SCOOTER = "Scooter"
    MOTORCYCLE = "Motorcycle"
    ROAD_SIDE_UNIT = "RoadSideUnit"
    CAMERA = "Camera"
    LIDAR = "Lidar"
    RADAR = "Radar"
    INDUCTIVE_LOOP = "InductiveLoop"
    MAGNETIC_SENSOR = "MagneticSensor"
    PLATFORM = "Platform"
    APPLICATION = "Application"
    NA = "NA"

    __str__ = str.__str__


ClientSubtypeOrStr: TypeAlias = Annotated[ClientSubtype | str, open_enum_validator(ClientSubtype)]
