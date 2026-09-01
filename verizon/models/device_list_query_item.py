from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class DeviceListQueryItem(SdkBaseModel):
    """The list of devices in the account."""

    device_id: Optional[str] = Field(default=UNSET, alias="deviceId")
    """Device IMEI."""

    mdn: Optional[str] = UNSET
    """The MDN (phone number) of the device."""

    model: Optional[str] = UNSET
    """The device model name."""

    make: Optional[str] = UNSET
    """The device make."""

    firmware: Optional[str] = UNSET
    """The name of the firmware image currently installed on the device."""

    fota_eligible: Optional[bool] = Field(default=UNSET, alias="fotaEligible")
    """True if the device firmware can be upgraded over the air using the Software Management Services API."""

    license_assigned: Optional[bool] = Field(default=UNSET, alias="licenseAssigned")
    """True if an MRC license has been assigned to this device."""

    upgrade_time: Optional[str] = Field(default=UNSET, alias="upgradeTime")
    """The date and time that the device firmware was last upgraded. If a device has never been upgraded, the
    upgradeTime will be 01/01/1900 0:0:0."""


class DeviceListQueryItemDict(TypedDict):
    device_id: NotRequired[str]
    mdn: NotRequired[str]
    model: NotRequired[str]
    make: NotRequired[str]
    firmware: NotRequired[str]
    fota_eligible: NotRequired[bool]
    license_assigned: NotRequired[bool]
    upgrade_time: NotRequired[str]
