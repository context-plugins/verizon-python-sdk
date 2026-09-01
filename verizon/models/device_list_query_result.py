from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .device_list_query_item import DeviceListQueryItem, DeviceListQueryItemDict


class DeviceListQueryResult(SdkBaseModel):
    """List of devices."""

    account_name: Optional[str] = Field(default=UNSET, alias="accountName")
    """Account identifier in "##########-#####"."""

    has_more_data: Optional[bool] = Field(default=UNSET, alias="hasMoreData")
    """True if there are more devices to retrieve."""

    last_seen_device_id: Optional[int] = Field(default=UNSET, alias="lastSeenDeviceId")
    """If hasMoreData=true, the startIndex to use for the next request. 0 if hasMoreData=false."""

    device_list: Optional[list[DeviceListQueryItem]] = Field(default=UNSET, alias="deviceList")
    """The list of devices in the account."""


class DeviceListQueryResultDict(TypedDict):
    account_name: NotRequired[str]
    has_more_data: NotRequired[bool]
    last_seen_device_id: NotRequired[int]
    device_list: NotRequired[list[DeviceListQueryItem | DeviceListQueryItemDict]]
