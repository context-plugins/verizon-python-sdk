from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .hpl_account_device_list import HplAccountDeviceList, HplAccountDeviceListDict
from .hpl_custom_fields import HplCustomFields, HplCustomFieldsDict


class HplAddDevicesRequest(SdkBaseModel):
    """Request to add the devices."""

    state: Optional[str] = UNSET
    """The initial service state for the devices. The only valid state is "Preactive."
    """

    devices_to_add: Optional[list[HplAccountDeviceList]] = Field(default=UNSET, alias="devicesToAdd")
    """The devices that you want to add."""

    account_name: Optional[str] = Field(default=UNSET, alias="accountName")
    """The numeric name of the account and must include leading zeroes."""

    custom_fields: Optional[list[HplCustomFields]] = Field(default=UNSET, alias="customFields")
    """The names and values for any custom fields that you want set for the devices as they are added to the account."""

    group_name: Optional[str] = Field(default=UNSET, alias="groupName")
    """The name of a device group to add the devices to. They are added to the default device group if you don't include
    this parameter."""

    sku_number: Optional[str] = Field(default=UNSET, alias="skuNumber")
    """The Stock Keeping Unit (SKU) number of a 4G device type with an embedded SIM."""

    smsr_oid: Optional[str] = Field(default=UNSET, alias="smsrOid")
    """The Subscription Manager Secure Router Object ID, used for remote SIM provisioning. SMSR securely routes the
    download and management of eSIM profiles."""

    number_of_virtual_imei: Optional[int] = Field(default=UNSET, alias="numberOfVirtualImei")
    """numberOfVirtualImei."""

    upload_type: Optional[str] = Field(default=UNSET, alias="uploadType")
    """uploadType."""


class HplAddDevicesRequestDict(TypedDict):
    state: NotRequired[str]
    devices_to_add: NotRequired[list[HplAccountDeviceList | HplAccountDeviceListDict]]
    account_name: NotRequired[str]
    custom_fields: NotRequired[list[HplCustomFields | HplCustomFieldsDict]]
    group_name: NotRequired[str]
    sku_number: NotRequired[str]
    smsr_oid: NotRequired[str]
    number_of_virtual_imei: NotRequired[int]
    upload_type: NotRequired[str]
