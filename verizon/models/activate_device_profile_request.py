from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .device_list import DeviceList, DeviceListDict


class ActivateDeviceProfileRequest(SdkBaseModel):
    devices: list[DeviceList]
    account_name: str = Field(alias="accountName")
    service_plan: Optional[str] = Field(default=UNSET, alias="servicePlan")
    mdn_zip_code: Optional[str] = Field(default=UNSET, alias="mdnZipCode")


class ActivateDeviceProfileRequestDict(TypedDict):
    devices: list[DeviceList | DeviceListDict]
    account_name: str
    service_plan: NotRequired[str]
    mdn_zip_code: NotRequired[str]
