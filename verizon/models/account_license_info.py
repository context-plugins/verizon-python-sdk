from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .account_license_device_list_item import AccountLicenseDeviceListItem, AccountLicenseDeviceListItemDict


class AccountLicenseInfo(SdkBaseModel):
    """Account license information."""

    account_name: Optional[str] = Field(default=UNSET, alias="accountName")
    """Account identifier in "##########-#####"."""

    total_licenses: Optional[int] = Field(default=UNSET, alias="totalLicenses")
    """Number of monthly licenses in an MRC subscription."""

    assigned_licenses: Optional[int] = Field(default=UNSET, alias="assignedLicenses")
    """Number of licenses currently assigned to devices."""

    has_more_data: Optional[bool] = Field(default=UNSET, alias="hasMoreData")
    """True if there are more devices to retrieve."""

    last_seen_device_id: Optional[int] = Field(default=UNSET, alias="lastSeenDeviceId")
    """If hasMoreData=true, the startIndex to use for the next request. 0 if hasMoreData=false."""

    device_list: Optional[list[AccountLicenseDeviceListItem]] = Field(default=UNSET, alias="deviceList")
    """The list of devices that have licenses assigned, including the date and time of when each license was
    assigned."""


class AccountLicenseInfoDict(TypedDict):
    account_name: NotRequired[str]
    total_licenses: NotRequired[int]
    assigned_licenses: NotRequired[int]
    has_more_data: NotRequired[bool]
    last_seen_device_id: NotRequired[int]
    device_list: NotRequired[list[AccountLicenseDeviceListItem | AccountLicenseDeviceListItemDict]]
