from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .custom_fields import CustomFields, CustomFieldsDict


class DeviceGroup(SdkBaseModel):
    """Returns a list of all device groups in a specified account."""

    description: Optional[str] = UNSET
    """The description of the device group."""

    extended_attributes: Optional[list[CustomFields]] = Field(default=UNSET, alias="extendedAttributes")
    """Any extended attributes for the device group, as Key and Value pairs."""

    is_default_group: Optional[bool] = Field(default=UNSET, alias="isDefaultGroup")
    """Identifies the default device group."""

    name: Optional[str] = UNSET
    """The name of the device group."""


class DeviceGroupDict(TypedDict):
    description: NotRequired[str]
    extended_attributes: NotRequired[list[CustomFields | CustomFieldsDict]]
    is_default_group: NotRequired[bool]
    name: NotRequired[str]
