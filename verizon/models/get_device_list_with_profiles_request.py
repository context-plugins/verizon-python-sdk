from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .giodevice_id import GiodeviceId, GiodeviceIdDict


class GetDeviceListWithProfilesRequest(SdkBaseModel):
    account_name: str = Field(alias="accountName")
    provisioning_status_filter: Optional[str] = Field(default=UNSET, alias="provisioningStatusFilter")
    profile_status_filter: Optional[str] = Field(default=UNSET, alias="profileStatusFilter")
    carrier_name_filter: Optional[str] = Field(default=UNSET, alias="carrierNameFilter")
    device_filter: Optional[list[GiodeviceId]] = Field(default=UNSET, alias="deviceFilter")


class GetDeviceListWithProfilesRequestDict(TypedDict):
    account_name: str
    provisioning_status_filter: NotRequired[str]
    profile_status_filter: NotRequired[str]
    carrier_name_filter: NotRequired[str]
    device_filter: NotRequired[list[GiodeviceId | GiodeviceIdDict]]
