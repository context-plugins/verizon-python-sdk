from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .device_id import DeviceId, DeviceIdDict


class Smsmessage(SdkBaseModel):
    """SMS messages sent by all M2M devices associated with a billing account."""

    device_ids: Optional[list[DeviceId]] = Field(default=UNSET, alias="deviceIds")
    """One or more IDs of the device that sent the message."""

    message: Optional[str] = UNSET
    """The contents of the SMS message."""

    timestamp: Optional[str] = UNSET
    """The date and time that the message was received by the Verizon ThingSpace Platform."""


class SmsmessageDict(TypedDict):
    device_ids: NotRequired[list[DeviceId | DeviceIdDict]]
    message: NotRequired[str]
    timestamp: NotRequired[str]
