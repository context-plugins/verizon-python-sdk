from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.client_subtype import ClientSubtypeOrStr
from .enums.etx_client_type import EtxClientTypeOrStr


class DevicesFilter(SdkBaseModel):
    """Optional filter criteria. Can specify one or more of:
    - ClientType: Filter devices by client type
    - ClientSubtype: Filter devices by client subtype
    - MecId: Filter devices by MEC ID
    - PageSize: Number of devices to return per page

    Valid combinations:
    - ClientType only
    - ClientSubtype only
    - ClientType and ClientSubtype together
    - MecId only
    - MecId and ClientType together
    - MecId and ClientSubtype together
    - MecId, ClientType, and ClientSubtype together
    - PageSize only
    - PageSize with any of the above combinations

    If no filter is provided, all devices for the vendor are returned."""

    client_type: Optional[EtxClientTypeOrStr] = Field(default=UNSET, alias="ClientType")
    """The type of the client that is to be registered. This is one of the major traffic participant groups considered
    in V2X communication. The system uses this value to define which topics the client will be able to publish and
    subscribe to.

    Values:
    - **Vehicle** - Vehicle with an enclosure around the passengers. (Subtypes: Motorcycle, PassengerCar, Truck, Bus,
        EmergencyVehicle, SchoolBus, MaintenanceVehicle)
    - **VulnerableRoadUser** - Traffic participants without a protecting enclosure. (Subtypes: Bicycle, Pedestrian,
        Scooter)
    - **TrafficLightController** - A Traffic light controller system. (Subtypes: NA)
    - **InfrastructureSensor** - Sensors that are deployed in the infrastructure. (Subtypes: RoadSideUnit, Camera,
        Lidar, Radar, InductiveLoop, MagneticSensor)
    - **OnboardSensor** - Sensors that are onboard on a vehicle(Subtypes: Camera, Lidar, Radar)
    - **Software** - A software system or application. (Subtypes: Platform, Application, NA)"""

    client_subtype: Optional[ClientSubtypeOrStr] = Field(default=UNSET, alias="ClientSubtype")
    """The subtype or subgroup of the client type. This further specifies the client type. For example it will specify
    if the client is a passenger car or a truck. See the ClientType description for the supported Subtypes for each
    client type."""

    mec_id: Optional[str] = Field(default=UNSET, alias="MecId")
    """The unique identifier for a Multi-access Edge Computing (MEC) location in the ETX system. This ID is used to
    reference and manage MEC locations for registration, update, retrieval, and deletion operations."""

    page_size: Optional[int] = Field(default=UNSET, alias="PageSize")
    """Number of devices to return per page. If not provided, the server default is used."""


class DevicesFilterDict(TypedDict):
    client_type: NotRequired[EtxClientTypeOrStr]
    client_subtype: NotRequired[ClientSubtypeOrStr]
    mec_id: NotRequired[str]
    page_size: NotRequired[int]
