from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .gbi_carrier_information5 import GbiCarrierInformation5, GbiCarrierInformation5Dict
from .group_name import GroupName, GroupNameDict
from .unions.custom_field import CustomField, CustomFieldDict
from .unions.device_id1 import DeviceId1, DeviceId1Dict
from .unions.extended_attribute import ExtendedAttribute, ExtendedAttributeDict


class GbiaccountNameobject5(SdkBaseModel):
    account_name: Optional[str] = Field(default=UNSET, alias="accountName")
    billing_cycle_end_date: Optional[str] = Field(default=UNSET, alias="billingCycleEndDate")
    carrier_information: Optional[list[GbiCarrierInformation5]] = Field(default=UNSET, alias="carrierInformation")
    connected: Optional[bool] = UNSET
    created_at: Optional[str] = Field(default=UNSET, alias="createdAt")
    custom_fields: Optional[list[CustomField]] = Field(default=UNSET, alias="customFields")
    device_ids: Optional[list[DeviceId1]] = Field(default=UNSET, alias="deviceIds")
    extended_attributes: Optional[list[ExtendedAttribute]] = Field(default=UNSET, alias="extendedAttributes")
    group_names: Optional[list[GroupName]] = Field(default=UNSET, alias="groupNames")
    ip_address: Optional[str] = Field(default=UNSET, alias="ipAddress")
    last_activation_by: Optional[str] = Field(default=UNSET, alias="lastActivationBy")
    last_activation_date: Optional[str] = Field(default=UNSET, alias="lastActivationDate")


class GbiaccountNameobject5Dict(TypedDict):
    account_name: NotRequired[str]
    billing_cycle_end_date: NotRequired[str]
    carrier_information: NotRequired[list[GbiCarrierInformation5 | GbiCarrierInformation5Dict]]
    connected: NotRequired[bool]
    created_at: NotRequired[str]
    custom_fields: NotRequired[list[CustomField | CustomFieldDict]]
    device_ids: NotRequired[list[DeviceId1 | DeviceId1Dict]]
    extended_attributes: NotRequired[list[ExtendedAttribute | ExtendedAttributeDict]]
    group_names: NotRequired[list[GroupName | GroupNameDict]]
    ip_address: NotRequired[str]
    last_activation_by: NotRequired[str]
    last_activation_date: NotRequired[str]
