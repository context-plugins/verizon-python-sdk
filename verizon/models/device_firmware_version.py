from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel


class DeviceFirmwareVersion(SdkBaseModel):
    """Device and firmware information."""

    status: Optional[str] = UNSET
    reason: Optional[str] = UNSET
    device_id: str = Field(alias="deviceId")
    """Device IMEI."""

    firmware_version: str = Field(alias="firmwareVersion")
    """Device Firmware Version."""

    firmware_version_update_time: Optional[RFC3339DateTime] = Field(default=UNSET, alias="firmwareVersionUpdateTime")


class DeviceFirmwareVersionDict(TypedDict):
    status: NotRequired[str]
    reason: NotRequired[str]
    device_id: str
    firmware_version: str
    firmware_version_update_time: NotRequired[RFC3339DateTime]
