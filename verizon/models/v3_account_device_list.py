from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .v3_account_device import V3AccountDevice, V3AccountDeviceDict


class V3AccountDeviceList(SdkBaseModel):
    """Array of devices."""

    account_name: str = Field(alias="accountName")
    """Account name."""

    has_more_data: bool = Field(alias="hasMoreData")
    """Has more device flag?"""

    last_seen_device_id: Optional[str] = Field(default=UNSET, alias="lastSeenDeviceId")
    """Last seen device identifier."""

    max_page_size: int = Field(alias="maxPageSize")
    """Maximum page size."""

    device_list: list[V3AccountDevice] = Field(alias="deviceList")
    """Account device list."""


class V3AccountDeviceListDict(TypedDict):
    account_name: str
    has_more_data: bool
    last_seen_device_id: NotRequired[str]
    max_page_size: int
    device_list: list[V3AccountDevice | V3AccountDeviceDict]
