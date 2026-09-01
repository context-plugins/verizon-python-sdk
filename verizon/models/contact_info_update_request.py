from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .account_device_list import AccountDeviceList, AccountDeviceListDict
from .place_of_use import PlaceOfUse, PlaceOfUseDict


class ContactInfoUpdateRequest(SdkBaseModel):
    """Request to update contact information."""

    primary_place_of_use: PlaceOfUse = Field(alias="primaryPlaceOfUse")
    """The customer name and the address of the device's primary place of use. Leave these fields empty to use the
    account profile address as the primary place of use. These values will be applied to all devices in the request.If
    the account is enabled for non-geographic MDNs and the device supports it, the primaryPlaceOfUse address will also
    be used to derive the MDN for the device."""

    account_name: Optional[str] = Field(default=UNSET, alias="accountName")
    """The name of the billing account that the devices belong to. An account name is usually numeric, and must include
    any leading zeros."""

    devices: Optional[list[AccountDeviceList]] = UNSET
    """A list of the devices that you want to change, specified by device identifier. You only need to provide one
    identifier per device. Do not include accountName, groupName, customFields, or servicePlan if you use this
    parameter."""


class ContactInfoUpdateRequestDict(TypedDict):
    primary_place_of_use: PlaceOfUse | PlaceOfUseDict
    account_name: NotRequired[str]
    devices: NotRequired[list[AccountDeviceList | AccountDeviceListDict]]
