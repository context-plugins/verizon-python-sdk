from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class FirmwareUpgradeDeviceListItem(SdkBaseModel):
    """A JSON object for each device that was included in the upgrade, showing the device IMEI, the status of the
    upgrade, and additional information about the status."""

    device_id: Optional[str] = Field(default=UNSET, alias="deviceId")
    """Device IMEI."""

    status: Optional[str] = UNSET
    """The status of the upgrade for this device."""

    result_reason: Optional[str] = Field(default=UNSET, alias="resultReason")
    """Additional details about the status. Not included when status='Request Pending.'"""


class FirmwareUpgradeDeviceListItemDict(TypedDict):
    device_id: NotRequired[str]
    status: NotRequired[str]
    result_reason: NotRequired[str]
