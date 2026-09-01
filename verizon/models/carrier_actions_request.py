from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .account_device_list import AccountDeviceList, AccountDeviceListDict
from .custom_fields import CustomFields, CustomFieldsDict


class CarrierActionsRequest(SdkBaseModel):
    """Request for a carrier action."""

    account_name: Optional[str] = Field(default=UNSET, alias="accountName")
    """The name of a billing account."""

    custom_fields: Optional[list[CustomFields]] = Field(default=UNSET, alias="customFields")
    """Custom field names and values, if you want to only include devices that have matching values."""

    devices: Optional[list[AccountDeviceList]] = UNSET
    """The devices for which you want to restore service, specified by device identifier."""

    with_billing: Optional[bool] = Field(default=UNSET, alias="withBilling")
    """set to "true" to suspend with billing, set to "false" to suspend without billing"""

    group_name: Optional[str] = Field(default=UNSET, alias="groupName")
    """The name of a device group, if you want to restore service for all devices in that group."""

    service_plan: Optional[str] = Field(default=UNSET, alias="servicePlan")
    """The name of a service plan, if you want to only include devices that have that service plan."""


class CarrierActionsRequestDict(TypedDict):
    account_name: NotRequired[str]
    custom_fields: NotRequired[list[CustomFields | CustomFieldsDict]]
    devices: NotRequired[list[AccountDeviceList | AccountDeviceListDict]]
    with_billing: NotRequired[bool]
    group_name: NotRequired[str]
    service_plan: NotRequired[str]
