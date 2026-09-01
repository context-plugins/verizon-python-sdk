from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .diagnostics_category import DiagnosticsCategory, DiagnosticsCategoryDict


class DeviceExtendedDiagnosticsResult(SdkBaseModel):
    """Result for a request to obtain device extended diagnostics."""

    categories: Optional[list[DiagnosticsCategory]] = UNSET
    """The response includes various types of information about the device, grouped into categories. Each category
    object contains the category name and a list of Extended Attribute objects as key-value pairs."""


class DeviceExtendedDiagnosticsResultDict(TypedDict):
    categories: NotRequired[list[DiagnosticsCategory | DiagnosticsCategoryDict]]
