from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .device_list import DeviceList, DeviceListDict


class SetFallbackAttributeRequest(SdkBaseModel):
    devices: list[DeviceList]
    account_name: str = Field(alias="accountName")
    carrier_name: Optional[str] = Field(default=UNSET, alias="carrierName")


class SetFallbackAttributeRequestDict(TypedDict):
    devices: list[DeviceList | DeviceListDict]
    account_name: str
    carrier_name: NotRequired[str]
