from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .unions.device_list_with_service_address import DeviceListWithServiceAddress, DeviceListWithServiceAddressDict


class GbichangeRequest5(SdkBaseModel):
    account_name: Optional[str] = Field(default=UNSET, alias="accountName")
    service_plan: Optional[str] = Field(default=UNSET, alias="servicePlan")
    device_list_with_service_address: Optional[list[DeviceListWithServiceAddress]] = Field(
        default=UNSET, alias="deviceListWithServiceAddress"
    )
    current_service_plan: Optional[str] = Field(default=UNSET, alias="currentServicePlan")


class GbichangeRequest5Dict(TypedDict):
    account_name: NotRequired[str]
    service_plan: NotRequired[str]
    device_list_with_service_address: NotRequired[list[DeviceListWithServiceAddress | DeviceListWithServiceAddressDict]]
    current_service_plan: NotRequired[str]
