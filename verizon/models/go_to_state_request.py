from __future__ import annotations

from typing import Any

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .account_device_list import AccountDeviceList, AccountDeviceListDict
from .custom_fields import CustomFields, CustomFieldsDict
from .device_filter import DeviceFilter, DeviceFilterDict
from .place_of_use import PlaceOfUse, PlaceOfUseDict


class GoToStateRequest(SdkBaseModel):
    """Changes the provisioning state of one or more devices to a specified customer-defined service and state."""

    service_name: str = Field(alias="serviceName")
    """The name of a customer-defined service to push the devices to."""

    state_name: str = Field(alias="stateName")
    """The name of a customer-defined stage state to push the devices to."""

    service_plan: str = Field(alias="servicePlan")
    """The service plan code that you want to assign to all specified devices in the new state."""

    mdn_zip_code: str = Field(alias="mdnZipCode")
    """The Zip code of the location where the line of service will primarily be used, or a Zip code that you have been
    told to use with these devices. For accounts that are configured for geographic numbering, this is the ZIP code from
    which the MDN will be derived."""

    devices: Optional[list[AccountDeviceList]] = UNSET
    """Up to 10,000 devices that you want to push to a different state, specified by device identifier."""

    filter: Optional[DeviceFilter] = UNSET
    """Specify the kind of the device identifier, the type of match, and the string that you want to match."""

    carrier_ip_pool_name: Optional[str] = Field(default=UNSET, alias="carrierIpPoolName")
    """The pool from which your device IP addresses will be derived if the service or state change requires new IP
    addresses.If you do not include this element, the default pool will be used."""

    public_ip_restriction: Optional[str] = Field(default=UNSET, alias="publicIpRestriction")
    """For devices with static IP addresses on the public network, this specifies whether the devices have general
    access to the Internet. Valid values are “restricted” or “unrestricted”."""

    sku_number: Optional[str] = Field(default=UNSET, alias="skuNumber")
    """The Stock Keeping Unit (SKU) number of a 4G device type with an embedded SIM. Can be used with ICCID or EID
    device identifiers in lieu of an IMEI when activating 4G devices. The SkuNumber will be used with all devices in the
    request, so all devices must be of the same type."""

    custom_fields: Optional[list[CustomFields]] = Field(default=UNSET, alias="customFields")
    """The names and values of any custom fields that you want to set for the devices."""

    devices_with_service_address: Optional[list[Any]] = Field(default=UNSET, alias="devicesWithServiceAddress")
    """This is an array that associates an IP address with a device identifier. This variable is only relevant for
    Business Internet/Fixed Wireless Access"""

    ip_address: Optional[str] = Field(default=UNSET, alias="ipAddress")
    """The IP address of the device."""

    group_name: Optional[str] = Field(default=UNSET, alias="groupName")
    """The name of a device group that the devices should be added to."""

    primary_place_of_use: Optional[PlaceOfUse] = Field(default=UNSET, alias="primaryPlaceOfUse")
    """The customer name and the address of the device's primary place of use. Leave these fields empty to use the
    account profile address as the primary place of use. These values will be applied to all devices in the request.If
    the account is enabled for non-geographic MDNs and the device supports it, the primaryPlaceOfUse address will also
    be used to derive the MDN for the device."""


class GoToStateRequestDict(TypedDict):
    service_name: str
    state_name: str
    service_plan: str
    mdn_zip_code: str
    devices: NotRequired[list[AccountDeviceList | AccountDeviceListDict]]
    filter: NotRequired[DeviceFilter | DeviceFilterDict]
    carrier_ip_pool_name: NotRequired[str]
    public_ip_restriction: NotRequired[str]
    sku_number: NotRequired[str]
    custom_fields: NotRequired[list[CustomFields | CustomFieldsDict]]
    devices_with_service_address: NotRequired[list[Any]]
    ip_address: NotRequired[str]
    group_name: NotRequired[str]
    primary_place_of_use: NotRequired[PlaceOfUse | PlaceOfUseDict]
