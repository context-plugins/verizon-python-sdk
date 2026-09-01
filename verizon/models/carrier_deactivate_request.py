from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .account_device_list import AccountDeviceList, AccountDeviceListDict
from .custom_fields import CustomFields, CustomFieldsDict


class CarrierDeactivateRequest(SdkBaseModel):
    """Request to deactivate a carrier."""

    account_name: str = Field(alias="accountName")
    """The name of a billing account."""

    devices: list[AccountDeviceList]
    """The devices for which you want to deactivate service, specified by device identifier."""

    reason_code: str = Field(alias="reasonCode")
    """Code identifying the reason for the deactivation. Currently the only valid reason code is “FF”, which corresponds
    to General Admin/Maintenance."""

    custom_fields: Optional[list[CustomFields]] = Field(default=UNSET, alias="customFields")
    """Custom field names and values, if you want to only include devices that have matching values."""

    etf_waiver: Optional[bool] = Field(default=UNSET, alias="etfWaiver")
    """Fees may be assessed for deactivating Verizon Wireless devices, depending on the account contract. The etfWaiver
    parameter waives the Early Termination Fee (ETF), if applicable."""

    group_name: Optional[str] = Field(default=UNSET, alias="groupName")
    """The name of a device group, if you want to deactivate all devices in that group."""

    service_plan: Optional[str] = Field(default=UNSET, alias="servicePlan")
    """The name of a service plan, if you want to only include devices that have that service plan."""

    delete_after_deactivation: Optional[bool] = Field(default=UNSET, alias="deleteAfterDeactivation")


class CarrierDeactivateRequestDict(TypedDict):
    account_name: str
    devices: list[AccountDeviceList | AccountDeviceListDict]
    reason_code: str
    custom_fields: NotRequired[list[CustomFields | CustomFieldsDict]]
    etf_waiver: NotRequired[bool]
    group_name: NotRequired[str]
    service_plan: NotRequired[str]
    delete_after_deactivation: NotRequired[bool]
