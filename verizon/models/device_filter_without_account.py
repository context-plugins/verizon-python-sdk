from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .custom_fields import CustomFields, CustomFieldsDict


class DeviceFilterWithoutAccount(SdkBaseModel):
    """Filter for devices without account."""

    group_name: Optional[str] = Field(default=UNSET, alias="groupName")
    """Only include devices that are in this device group."""

    service_plan: Optional[str] = Field(default=UNSET, alias="servicePlan")
    """Only include devices that have this service plan."""

    custom_fields: Optional[list[CustomFields]] = Field(default=UNSET, alias="customFields")
    """Custom field names and values, if you want to only include devices that have matching values."""


class DeviceFilterWithoutAccountDict(TypedDict):
    group_name: NotRequired[str]
    service_plan: NotRequired[str]
    custom_fields: NotRequired[list[CustomFields | CustomFieldsDict]]
