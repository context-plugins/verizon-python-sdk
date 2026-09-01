from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class DeviceUpgradeHistory(SdkBaseModel):
    """Firmware upgrade information."""

    device_id: Optional[str] = Field(default=UNSET, alias="deviceId")
    """Device IMEI."""

    id: Optional[str] = UNSET
    """The unique identifier for the upgrade."""

    account_name: Optional[str] = Field(default=UNSET, alias="accountName")
    """The name (number) of the billing account that the device belongs to."""

    firmware_from: Optional[str] = Field(default=UNSET, alias="firmwareFrom")
    """The firmware version that was on the device before the upgrade."""

    firmware_to: Optional[str] = Field(default=UNSET, alias="firmwareTo")
    """The name of the firmware version that was on the device after the upgrade."""

    start_date: Optional[str] = Field(default=UNSET, alias="startDate")
    """The date of the upgrade."""

    upgrade_start_time: Optional[str] = Field(default=UNSET, alias="upgradeStartTime")
    """The date and time that the upgrade actually started for this device."""

    status: Optional[str] = UNSET
    """The status of the upgrade for this device."""

    reason: Optional[str] = UNSET
    """More information about the status."""


class DeviceUpgradeHistoryDict(TypedDict):
    device_id: NotRequired[str]
    id: NotRequired[str]
    account_name: NotRequired[str]
    firmware_from: NotRequired[str]
    firmware_to: NotRequired[str]
    start_date: NotRequired[str]
    upgrade_start_time: NotRequired[str]
    status: NotRequired[str]
    reason: NotRequired[str]
