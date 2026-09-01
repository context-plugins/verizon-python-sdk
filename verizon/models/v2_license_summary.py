from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .v2_license_device import V2LicenseDevice, V2LicenseDeviceDict


class V2LicenseSummary(SdkBaseModel):
    """Summary of license assignment."""

    account_name: str = Field(alias="accountName")
    """Account identifier."""

    total_license: Optional[int] = Field(default=UNSET, alias="totalLicense")
    """Total FOTA license count."""

    assigned_licenses: int = Field(alias="assignedLicenses")
    """Assigned FOTA license count."""

    has_more_data: bool = Field(alias="hasMoreData")
    """True if there are more devices to retrieve."""

    last_seen_device_id: Optional[str] = Field(default=UNSET, alias="lastSeenDeviceId")
    """Last seen device identifier."""

    max_page_size: int = Field(alias="maxPageSize")
    """Maximum page size."""

    device_list: Optional[list[V2LicenseDevice]] = Field(default=UNSET, alias="deviceList")
    """Device IMEI list."""


class V2LicenseSummaryDict(TypedDict):
    account_name: str
    total_license: NotRequired[int]
    assigned_licenses: int
    has_more_data: bool
    last_seen_device_id: NotRequired[str]
    max_page_size: int
    device_list: NotRequired[list[V2LicenseDevice | V2LicenseDeviceDict]]
