from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Date, Optional, SdkBaseModel


class DeviceFirmwareUpgrade(SdkBaseModel):
    """Firmware upgrades information."""

    device_id: str = Field(alias="deviceId")
    """Device identifier."""

    campaign_id: str = Field(alias="campaignId")
    """Campaign identifier."""

    account_name: str = Field(alias="accountName")
    """Account identifier."""

    firmware_name: Optional[str] = Field(default=UNSET, alias="firmwareName")
    """Firmware name."""

    firmware_from: Optional[str] = Field(default=UNSET, alias="firmwareFrom")
    """Old firmware version."""

    firmware_to: Optional[str] = Field(default=UNSET, alias="firmwareTo")
    """New firmware version."""

    start_date: Date = Field(alias="startDate")
    """Firmware upgrade start date."""

    status: str
    """Firmware upgrade status."""

    reason: str
    """Software upgrade result reason."""

    report_updated_time: Optional[str] = Field(default=UNSET, alias="reportUpdatedTime")
    """Report updated time."""


class DeviceFirmwareUpgradeDict(TypedDict):
    device_id: str
    campaign_id: str
    account_name: str
    firmware_name: NotRequired[str]
    firmware_from: NotRequired[str]
    firmware_to: NotRequired[str]
    start_date: Date
    status: str
    reason: str
    report_updated_time: NotRequired[str]
