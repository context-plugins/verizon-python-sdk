from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .device_list2 import DeviceList2, DeviceList2Dict


class ProfileRequest2(SdkBaseModel):
    devices: Optional[list[DeviceList2]] = UNSET
    account_name: Optional[str] = Field(default=UNSET, alias="accountName")
    carrier_name: Optional[str] = Field(default=UNSET, alias="carrierName")
    reason_code: Optional[str] = Field(default=UNSET, alias="reasonCode")
    etf_waiver: Optional[bool] = Field(default=UNSET, alias="etfWaiver")
    check_fallback_profile: Optional[bool] = Field(default=UNSET, alias="checkFallbackProfile")


class ProfileRequest2Dict(TypedDict):
    devices: NotRequired[list[DeviceList2 | DeviceList2Dict]]
    account_name: NotRequired[str]
    carrier_name: NotRequired[str]
    reason_code: NotRequired[str]
    etf_waiver: NotRequired[bool]
    check_fallback_profile: NotRequired[bool]
