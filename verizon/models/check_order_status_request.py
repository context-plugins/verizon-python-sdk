from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .device_list import DeviceList, DeviceListDict


class CheckOrderStatusRequest(SdkBaseModel):
    """The request body identifies the devices to upload."""

    account_name: str = Field(alias="accountName")
    """The name of a billing account. An account name is usually numeric, and must include any leading zeros."""

    order_request_id: Optional[str] = Field(default=UNSET, alias="orderRequestId")
    """The request id from the activation order."""

    devices: list[DeviceList]
    """The devices to upload, specified by device IDs in a format matching uploadType."""


class CheckOrderStatusRequestDict(TypedDict):
    account_name: str
    order_request_id: NotRequired[str]
    devices: list[DeviceList | DeviceListDict]
