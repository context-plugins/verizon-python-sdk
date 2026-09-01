from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .v1_device_list_item import V1DeviceListItem, V1DeviceListItemDict


class V1LicensesAssignedRemovedResult(SdkBaseModel):
    """License assignment or removal confirmation."""

    account_name: Optional[str] = Field(default=UNSET, alias="accountName")
    """Account identifier in "##########-#####"."""

    lic_count: Optional[int] = Field(default=UNSET, alias="licCount")
    """Total number of monthly licenses in an MRC subscription."""

    lic_used_count: Optional[int] = Field(default=UNSET, alias="licUsedCount")
    """Number of licenses assigned to devices after the request completed."""

    device_list: Optional[list[V1DeviceListItem]] = Field(default=UNSET, alias="deviceList")
    """A JSON object for each device that was in the request."""


class V1LicensesAssignedRemovedResultDict(TypedDict):
    account_name: NotRequired[str]
    lic_count: NotRequired[int]
    lic_used_count: NotRequired[int]
    device_list: NotRequired[list[V1DeviceListItem | V1DeviceListItemDict]]
