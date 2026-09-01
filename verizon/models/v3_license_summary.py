from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .v3_license_device import V3LicenseDevice, V3LicenseDeviceDict


class V3LicenseSummary(SdkBaseModel):
    """Information for FOTA licenses assigned to devices."""

    account_name: str = Field(alias="accountName")
    """Account identifier."""

    total_licenses: Optional[int] = Field(default=UNSET, alias="totalLicenses")
    """Total FOTA license count."""

    assigned_licenses: int = Field(alias="assignedLicenses")
    """Assigned FOTA license count."""

    has_more_data: bool = Field(alias="hasMoreData")
    """True if there are more devices to retrieve."""

    last_seen_device_id: Optional[str] = Field(default=UNSET, alias="lastSeenDeviceId")
    """Last seen device identifier."""

    max_page_size: int = Field(alias="maxPageSize")
    """Maximum page size."""

    device_list: Optional[list[V3LicenseDevice]] = Field(default=UNSET, alias="deviceList")
    """Device IMEI list."""


class V3LicenseSummaryDict(TypedDict):
    account_name: str
    total_licenses: NotRequired[int]
    assigned_licenses: int
    has_more_data: bool
    last_seen_device_id: NotRequired[str]
    max_page_size: int
    device_list: NotRequired[list[V3LicenseDevice | V3LicenseDeviceDict]]
