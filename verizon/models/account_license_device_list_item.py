from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel


class AccountLicenseDeviceListItem(SdkBaseModel):
    """The list of devices that have licenses assigned, including the date and time of when each license was
    assigned."""

    device_id: Optional[str] = Field(default=UNSET, alias="deviceId")
    """Device IMEI."""

    assignment_time: Optional[RFC3339DateTime] = Field(default=UNSET, alias="assignmentTime")
    """Timestamp of when a license was assigned to the device."""


class AccountLicenseDeviceListItemDict(TypedDict):
    device_id: NotRequired[str]
    assignment_time: NotRequired[RFC3339DateTime]
