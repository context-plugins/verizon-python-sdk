from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .giodevice_list import GiodeviceList, GiodeviceListDict


class DeviceProfileRequest(SdkBaseModel):
    devices: Optional[list[GiodeviceList]] = UNSET
    account_name: Optional[str] = Field(default=UNSET, alias="accountName")
    service_plan: Optional[str] = Field(default=UNSET, alias="servicePlan")


class DeviceProfileRequestDict(TypedDict):
    devices: NotRequired[list[GiodeviceList | GiodeviceListDict]]
    account_name: NotRequired[str]
    service_plan: NotRequired[str]
