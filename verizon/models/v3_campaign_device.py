from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .v3_device_status import V3DeviceStatus, V3DeviceStatusDict


class V3CampaignDevice(SdkBaseModel):
    """Campaign history."""

    total_device: Optional[int] = Field(default=UNSET, alias="totalDevice")
    """Total device count."""

    has_more_data: bool = Field(alias="hasMoreData")
    """Has more report flag."""

    last_seen_device_id: Optional[str] = Field(default=UNSET, alias="lastSeenDeviceId")
    """Device identifier."""

    max_page_size: int = Field(alias="maxPageSize")
    """Maximum page size."""

    device_list: list[V3DeviceStatus] = Field(alias="deviceList")
    """List of devices with id in IMEI."""


class V3CampaignDeviceDict(TypedDict):
    total_device: NotRequired[int]
    has_more_data: bool
    last_seen_device_id: NotRequired[str]
    max_page_size: int
    device_list: list[V3DeviceStatus | V3DeviceStatusDict]
