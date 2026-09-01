from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .giodevice_list import GiodeviceList, GiodeviceListDict


class GiodeactivateDeviceProfileRequest(SdkBaseModel):
    devices: Optional[list[GiodeviceList]] = UNSET
    account_name: Optional[str] = Field(default=UNSET, alias="accountName")
    service_plan: Optional[str] = Field(default=UNSET, alias="servicePlan")
    etf_waiver: Optional[bool] = Field(default=UNSET, alias="etfWaiver")
    reason_code: Optional[str] = Field(default=UNSET, alias="reasonCode")


class GiodeactivateDeviceProfileRequestDict(TypedDict):
    devices: NotRequired[list[GiodeviceList | GiodeviceListDict]]
    account_name: NotRequired[str]
    service_plan: NotRequired[str]
    etf_waiver: NotRequired[bool]
    reason_code: NotRequired[str]
