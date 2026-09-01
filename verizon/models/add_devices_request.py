from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .account_device_list import AccountDeviceList, AccountDeviceListDict
from .custom_fields import CustomFields, CustomFieldsDict


class AddDevicesRequest(SdkBaseModel):
    """Request to add the devices."""

    state: str
    """The initial service state for the devices. The only valid state is “Pre-active.”"""

    devices_to_add: list[AccountDeviceList] = Field(alias="devicesToAdd")
    """The devices that you want to add."""

    account_name: Optional[str] = Field(default=UNSET, alias="accountName")
    """The billing account to which the devices are added."""

    custom_fields: Optional[list[CustomFields]] = Field(default=UNSET, alias="customFields")
    """The names and values for any custom fields that you want set for the devices as they are added to the account."""

    group_name: Optional[str] = Field(default=UNSET, alias="groupName")
    """The name of a device group to add the devices to. They are added to the default device group if you don't include
    this parameter."""

    sku_number: Optional[str] = Field(default=UNSET, alias="skuNumber")
    """The Stock Keeping Unit (SKU) number of a 4G device type with an embedded SIM."""

    smsr_oid: Optional[str] = Field(default=UNSET, alias="smsrOid")


class AddDevicesRequestDict(TypedDict):
    state: str
    devices_to_add: list[AccountDeviceList | AccountDeviceListDict]
    account_name: NotRequired[str]
    custom_fields: NotRequired[list[CustomFields | CustomFieldsDict]]
    group_name: NotRequired[str]
    sku_number: NotRequired[str]
    smsr_oid: NotRequired[str]
