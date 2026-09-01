from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .search_device_by_property_fields import SearchDeviceByPropertyFields, SearchDeviceByPropertyFieldsDict


class Fields1(SdkBaseModel):
    item: Optional[SearchDeviceByPropertyFields] = UNSET
    """List of device sensors and their most recently reported values."""


class Fields1Dict(TypedDict):
    item: NotRequired[SearchDeviceByPropertyFields | SearchDeviceByPropertyFieldsDict]
