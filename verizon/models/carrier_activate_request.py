from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .account_device_list import AccountDeviceList, AccountDeviceListDict
from .custom_fields import CustomFields, CustomFieldsDict
from .place_of_use import PlaceOfUse, PlaceOfUseDict


class CarrierActivateRequest(SdkBaseModel):
    """Request for carrier activation."""

    devices: list[AccountDeviceList]
    """Up to 10,000 devices for which you want to activate service, specified by device identifier."""

    service_plan: str = Field(alias="servicePlan")
    """The service plan code that you want to assign to all specified devices."""

    mdn_zip_code: str = Field(alias="mdnZipCode")
    """The Zip code of the location where the line of service will primarily be used, or a Zip code that you have been
    told to use with these devices. For accounts that are configured for geographic numbering, this is the ZIP code from
    which the MDN will be derived."""

    account_name: Optional[str] = Field(default=UNSET, alias="accountName")
    """The name of a billing account."""

    carrier_ip_pool_name: Optional[str] = Field(default=UNSET, alias="carrierIpPoolName")
    """The private IP pool (Carrier Group Name) from which your device IP addresses will be derived."""

    carrier_name: Optional[str] = Field(default=UNSET, alias="carrierName")
    """The carrier that will perform the activation."""

    cost_center_code: Optional[str] = Field(default=UNSET, alias="costCenterCode")
    """A string to identify the cost center that the device is associated with."""

    custom_fields: Optional[list[CustomFields]] = Field(default=UNSET, alias="customFields")
    """A user-defined descriptive field, limited to 50 characters."""

    group_name: Optional[str] = Field(default=UNSET, alias="groupName")
    """If you specify devices by ID in the devices parameters, this is the name of a device group that the devices
    should be added to.If you don't specify individual devices with the devices parameter, you can provide the name of a
    device group to activate all devices in that group."""

    lead_id: Optional[str] = Field(default=UNSET, alias="leadId")
    """The ID of a “Qualified” or “Closed - Won” VPP customer lead, which is used with other values to determine MDN
    assignment, taxation, and compensation."""

    primary_place_of_use: Optional[PlaceOfUse] = Field(default=UNSET, alias="primaryPlaceOfUse")
    """The customer name and the address of the device's primary place of use. Leave these fields empty to use the
    account profile address as the primary place of use. These values will be applied to all devices in the request.If
    the account is enabled for non-geographic MDNs and the device supports it, the primaryPlaceOfUse address will also
    be used to derive the MDN for the device."""

    public_ip_restriction: Optional[str] = Field(default=UNSET, alias="publicIpRestriction")
    """For devices with static IP addresses on the public network, this specifies whether the devices have general
    access to the Internet."""

    sku_number: Optional[str] = Field(default=UNSET, alias="skuNumber")
    """The Stock Keeping Unit (SKU) of a 4G device type can be used with ICCID device identifiers in lieu of an IMEI
    when activating 4G devices. The SkuNumber will be used with all devices in the request, so all devices must be of
    the same type."""


class CarrierActivateRequestDict(TypedDict):
    devices: list[AccountDeviceList | AccountDeviceListDict]
    service_plan: str
    mdn_zip_code: str
    account_name: NotRequired[str]
    carrier_ip_pool_name: NotRequired[str]
    carrier_name: NotRequired[str]
    cost_center_code: NotRequired[str]
    custom_fields: NotRequired[list[CustomFields | CustomFieldsDict]]
    group_name: NotRequired[str]
    lead_id: NotRequired[str]
    primary_place_of_use: NotRequired[PlaceOfUse | PlaceOfUseDict]
    public_ip_restriction: NotRequired[str]
    sku_number: NotRequired[str]
