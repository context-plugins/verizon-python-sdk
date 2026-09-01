from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .custom_fields import CustomFields, CustomFieldsDict


class DiagnosticsCategory(SdkBaseModel):
    """Various types of information about the device, grouped into categories. Each category object contains the
    category name and a list of Extended Attribute objects as key-value pairs."""

    category_name: Optional[str] = Field(default=UNSET, alias="categoryName")
    """The name of the category."""

    extended_attributes: Optional[list[CustomFields]] = Field(default=UNSET, alias="extendedAttributes")
    """A list of Extended Attribute objects as key-value pairs."""


class DiagnosticsCategoryDict(TypedDict):
    category_name: NotRequired[str]
    extended_attributes: NotRequired[list[CustomFields | CustomFieldsDict]]
