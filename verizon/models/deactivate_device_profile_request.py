from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .deactivate_device_list import DeactivateDeviceList, DeactivateDeviceListDict


class DeactivateDeviceProfileRequest(SdkBaseModel):
    account_name: str = Field(alias="accountName")
    reason_code: str = Field(alias="reasonCode")
    devices: Optional[list[DeactivateDeviceList]] = UNSET
    carrier_name: Optional[str] = Field(default=UNSET, alias="carrierName")
    etf_waiver: Optional[bool] = Field(default=UNSET, alias="etfWaiver")
    check_fallback_profile: Optional[bool] = Field(default=UNSET, alias="checkFallbackProfile")


class DeactivateDeviceProfileRequestDict(TypedDict):
    account_name: str
    reason_code: str
    devices: NotRequired[list[DeactivateDeviceList | DeactivateDeviceListDict]]
    carrier_name: NotRequired[str]
    etf_waiver: NotRequired[bool]
    check_fallback_profile: NotRequired[bool]
