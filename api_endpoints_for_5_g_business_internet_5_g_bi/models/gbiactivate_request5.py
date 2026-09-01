from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .unions.device_list_with_service_address1 import DeviceListWithServiceAddress1, DeviceListWithServiceAddress1Dict


class GbiactivateRequest5(SdkBaseModel):
    account_name: Optional[str] = Field(default=UNSET, alias="accountName")
    service_plan: Optional[str] = Field(default=UNSET, alias="servicePlan")
    device_list_with_service_address: Optional[list[DeviceListWithServiceAddress1]] = Field(
        default=UNSET, alias="deviceListWithServiceAddress"
    )
    sku_number: Optional[str] = Field(default=UNSET, alias="skuNumber")
    public_ip_restriction: Optional[str] = Field(default=UNSET, alias="publicIpRestriction")
    carrier_name: Optional[str] = Field(default=UNSET, alias="carrierName")
    mdn_zip_code: Optional[str] = Field(default=UNSET, alias="mdnZipCode")


class GbiactivateRequest5Dict(TypedDict):
    account_name: NotRequired[str]
    service_plan: NotRequired[str]
    device_list_with_service_address: NotRequired[
        list[DeviceListWithServiceAddress1 | DeviceListWithServiceAddress1Dict]
    ]
    sku_number: NotRequired[str]
    public_ip_restriction: NotRequired[str]
    carrier_name: NotRequired[str]
    mdn_zip_code: NotRequired[str]
