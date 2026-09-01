from __future__ import annotations

from uuid import UUID

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class EtxclientIdlookup(SdkBaseModel):
    """Lookup object for identifying an ETX client. One of the following IDs is required: DeviceID, IMEI, ICCID, or
    IMSI. If more than one ID is provided, the API will use the first ID found in the following order: DeviceID, IMEI,
    ICCID, IMSI."""

    device_id: Optional[UUID] = Field(default=UNSET, alias="DeviceID")
    """The generated ID (UUID v4) for the device. It can be used as:
      - the MQTT Client ID when connecting to the Message Exchange system
      - a parameter when asking for the connection endpoint
      - a parameter when finishing the device registration
      - a parameter when unregistering the device"""

    imei: Optional[str] = Field(default=UNSET, alias="IMEI")
    """The IMEI number of the device."""

    iccid: Optional[str] = Field(default=UNSET, alias="ICCID")
    """The ICCID number of the device."""

    imsi: Optional[str] = Field(default=UNSET, alias="IMSI")
    """The IMSI number of the device."""


class EtxclientIdlookupDict(TypedDict):
    device_id: NotRequired[UUID]
    imei: NotRequired[str]
    iccid: NotRequired[str]
    imsi: NotRequired[str]
