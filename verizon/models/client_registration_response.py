from __future__ import annotations

from uuid import UUID

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .certificate import Certificate, CertificateDict


class ClientRegistrationResponse(SdkBaseModel):
    """Response for /clients/registration. It provides a generated device ID and the certificates needed to connect the
    ETX Message Exchange."""

    device_id: UUID = Field(alias="DeviceID")
    """The generated ID (UUID v4) for the device. It can be used as:
      - the MQTT Client ID when connecting to the Message Exchange system
      - a parameter when asking for the connection endpoint
      - a parameter when finishing the device registration
      - a parameter when unregistering the device"""

    certificate: Certificate = Field(alias="Certificate")
    """Structure for the credentials required to connect to the ETX MQTT Message Exchange."""


class ClientRegistrationResponseDict(TypedDict):
    device_id: UUID
    certificate: Certificate | CertificateDict
