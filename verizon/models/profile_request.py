from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .device_list import DeviceList, DeviceListDict
from .unions.primary_place_of_use import PrimaryPlaceOfUse, PrimaryPlaceOfUseDict


class ProfileRequest(SdkBaseModel):
    account_name: str = Field(alias="accountName")
    devices: list[DeviceList]
    carrier_name: Optional[str] = Field(default=UNSET, alias="carrierName")
    service_plan: Optional[str] = Field(default=UNSET, alias="servicePlan")
    mdn_zip_code: Optional[str] = Field(default=UNSET, alias="mdnZipCode")
    primary_place_of_use: Optional[list[PrimaryPlaceOfUse]] = Field(default=UNSET, alias="primaryPlaceOfUse")
    smsr_oid: Optional[str] = Field(default=UNSET, alias="smsrOid")
    carrier_ip_pool_name: Optional[str] = Field(default=UNSET, alias="carrierIpPoolName")
    """The name of the pool of IP addresses assigned to the profile."""


class ProfileRequestDict(TypedDict):
    account_name: str
    devices: list[DeviceList | DeviceListDict]
    carrier_name: NotRequired[str]
    service_plan: NotRequired[str]
    mdn_zip_code: NotRequired[str]
    primary_place_of_use: NotRequired[list[PrimaryPlaceOfUse | PrimaryPlaceOfUseDict]]
    smsr_oid: NotRequired[str]
    carrier_ip_pool_name: NotRequired[str]
