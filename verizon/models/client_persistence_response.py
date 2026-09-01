from __future__ import annotations

from uuid import UUID

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .certificate import Certificate, CertificateDict
from .enums.client_subtype import ClientSubtypeOrStr
from .enums.etx_client_type import EtxClientTypeOrStr


class ClientPersistenceResponse(SdkBaseModel):
    """Response for /v2/clients/registration. It provides a generated device ID and the certificates needed to connect
    the ETX Message Exchange."""

    device_id: Optional[UUID] = Field(default=UNSET, alias="DeviceID")
    """The generated ID (UUID v4) for the device. It can be used as:
      - the MQTT Client ID when connecting to the Message Exchange system
      - a parameter when asking for the connection endpoint
      - a parameter when finishing the device registration
      - a parameter when unregistering the device"""

    certificate: Optional[Certificate] = Field(default=UNSET, alias="Certificate")
    """Structure for the credentials required to connect to the ETX MQTT Message Exchange."""

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

    vendor_id: Optional[str] = Field(default=UNSET, alias="VendorID")
    """The ID the vendor wants its devices to be registered under. E.g. Verizon, GM, Ford, etc."""


class ClientPersistenceResponseDict(TypedDict):
    device_id: NotRequired[UUID]
    certificate: NotRequired[Certificate | CertificateDict]
    client_type: NotRequired[EtxClientTypeOrStr]
    client_subtype: NotRequired[ClientSubtypeOrStr]
    vendor_id: NotRequired[str]
