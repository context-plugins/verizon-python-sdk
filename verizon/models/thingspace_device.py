from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .carrier_information import CarrierInformation, CarrierInformationDict
from .custom_fields import CustomFields, CustomFieldsDict
from .device_id import DeviceId, DeviceIdDict


class ThingspaceDevice(SdkBaseModel):
    """Device that exist in Verizon Mobile Device Management (MDM)."""

    account_name: Optional[str] = Field(default=UNSET, alias="accountName")
    """The billing account that the device is associated with."""

    billing_cycle_end_date: Optional[str] = Field(default=UNSET, alias="billingCycleEndDate")
    """The date that the device's current billing cycle ends."""

    carrier_informations: Optional[list[CarrierInformation]] = Field(default=UNSET, alias="carrierInformations")
    """The carrier information associated with the device."""

    connected: Optional[bool] = UNSET
    """True if the device is connected; false if it is not."""

    created_at: Optional[str] = Field(default=UNSET, alias="createdAt")
    """The date and time that the device was added to the system."""

    custom_fields: Optional[list[CustomFields]] = Field(default=UNSET, alias="customFields")
    """The custom fields and values that have been set for the device."""

    device_ids: Optional[list[DeviceId]] = Field(default=UNSET, alias="deviceIds")
    """All identifiers for the device."""

    extended_attributes: Optional[list[CustomFields]] = Field(default=UNSET, alias="extendedAttributes")
    """Any extended attributes for the device, as Key and Value pairs. The pairs listed below are returned as part of
    the response for a single device, but are not included if the request was for information about multiple devices."""

    group_names: OptionalNullable[list[str]] = Field(default=UNSET, alias="groupNames")
    """The device groups that the device belongs to."""

    ip_address: Optional[str] = Field(default=UNSET, alias="ipAddress")
    """The IP address of the device."""

    last_activation_by: Optional[str] = Field(default=UNSET, alias="lastActivationBy")
    """The user who last activated the device."""

    last_activation_date: Optional[str] = Field(default=UNSET, alias="lastActivationDate")
    """The date and time that the device was last activated."""

    last_connection_date: Optional[str] = Field(default=UNSET, alias="lastConnectionDate")
    """The most recent connection date and time."""


class ThingspaceDeviceDict(TypedDict):
    account_name: NotRequired[str]
    billing_cycle_end_date: NotRequired[str]
    carrier_informations: NotRequired[list[CarrierInformation | CarrierInformationDict]]
    connected: NotRequired[bool]
    created_at: NotRequired[str]
    custom_fields: NotRequired[list[CustomFields | CustomFieldsDict]]
    device_ids: NotRequired[list[DeviceId | DeviceIdDict]]
    extended_attributes: NotRequired[list[CustomFields | CustomFieldsDict]]
    group_names: NotRequired[list[str] | None]
    ip_address: NotRequired[str]
    last_activation_by: NotRequired[str]
    last_activation_date: NotRequired[str]
    last_connection_date: NotRequired[str]
