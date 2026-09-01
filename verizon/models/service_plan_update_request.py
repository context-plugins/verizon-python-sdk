from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel
from .account_device_list import AccountDeviceList, AccountDeviceListDict
from .custom_fields import CustomFields, CustomFieldsDict


class ServicePlanUpdateRequest(SdkBaseModel):
    """Request to update service plan."""

    service_plan: str = Field(alias="servicePlan")
    """The service plan code that you want to assign to all specified devices."""

    account_name: Optional[str] = Field(default=UNSET, alias="accountName")
    """The name of a billing account."""

    current_service_plan: Optional[str] = Field(default=UNSET, alias="currentServicePlan")
    """The name of a service plan, if you want to only include devices that have that service plan."""

    custom_fields: Optional[list[CustomFields]] = Field(default=UNSET, alias="customFields")
    """Custom field names and values, if you want to only include devices that have matching values."""

    devices: Optional[list[AccountDeviceList]] = UNSET
    """A list of the devices that you want to change, specified by device identifier."""

    group_name: Optional[str] = Field(default=UNSET, alias="groupName")
    """The name of a device group, if you want to restore service for all devices in that group."""

    carrier_ip_pool_name: Optional[str] = Field(default=UNSET, alias="carrierIpPoolName")
    take_effect: Optional[RFC3339DateTime] = Field(default=UNSET, alias="takeEffect")


class ServicePlanUpdateRequestDict(TypedDict):
    service_plan: str
    account_name: NotRequired[str]
    current_service_plan: NotRequired[str]
    custom_fields: NotRequired[list[CustomFields | CustomFieldsDict]]
    devices: NotRequired[list[AccountDeviceList | AccountDeviceListDict]]
    group_name: NotRequired[str]
    carrier_ip_pool_name: NotRequired[str]
    take_effect: NotRequired[RFC3339DateTime]
