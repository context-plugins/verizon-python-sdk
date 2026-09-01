from __future__ import annotations

from uuid import UUID

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class ClientRegistrationPendingResponse(SdkBaseModel):
    """Response for /clients/registration for pending state. It provides a device_id for user to finish registration
    with PUT API call"""

    device_id: UUID = Field(alias="DeviceID")
    """The generated ID (UUID v4) for the device. It can be used as:
      - the MQTT Client ID when connecting to the Message Exchange system
      - a parameter when asking for the connection endpoint
      - a parameter when finishing the device registration
      - a parameter when unregistering the device"""

    message: str = Field(alias="Message")
    """The reason why the registration is in pending state"""


class ClientRegistrationPendingResponseDict(TypedDict):
    device_id: UUID
    message: str
