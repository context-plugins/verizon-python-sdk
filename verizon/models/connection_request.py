from __future__ import annotations

from uuid import UUID

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.network_type import NetworkTypeOrStr
from .geolocation import Geolocation, GeolocationDict


class ConnectionRequest(SdkBaseModel):
    """Request for /clients/connection. It requires the device ID acquired in the registration request call; the
    geolocation of the device at the time of the request; and the network type (Verizon or non-Verizon). The system uses
    this information to determine with MQTT endpoint the device should use to connect the ETX Message Exchange."""

    device_id: UUID = Field(alias="DeviceID")
    """The generated ID (UUID v4) for the device. It can be used as:
      - the MQTT Client ID when connecting to the Message Exchange system
      - a parameter when asking for the connection endpoint
      - a parameter when finishing the device registration
      - a parameter when unregistering the device"""

    geolocation: Geolocation = Field(alias="Geolocation")
    """Geolocation of the device at the time of the connection request in GPS coordinates."""

    network_type: NetworkTypeOrStr = Field(alias="NetworkType")
    """The type of the device's network connection at the time of the request. If the device is on the Verizon cellular
    network it should use the "VZ" value otherwise the "non-VZ" value.

    Devices on the Verizon network can directly access the ETX Message Exchange on the MEC (Mobile Edge Compute
    server)"""


class ConnectionRequestDict(TypedDict):
    device_id: UUID
    geolocation: Geolocation | GeolocationDict
    network_type: NetworkTypeOrStr
