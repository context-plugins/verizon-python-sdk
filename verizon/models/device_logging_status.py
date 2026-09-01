from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import Date, SdkBaseModel


class DeviceLoggingStatus(SdkBaseModel):
    """Device logging status information."""

    device_id: str = Field(alias="deviceId")
    """Device IMEI."""

    expiry_date: Date = Field(alias="expiryDate")
    """The date when device logging expires."""


class DeviceLoggingStatusDict(TypedDict):
    device_id: str
    expiry_date: Date
