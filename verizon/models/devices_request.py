from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .unions.filter import Filter, FilterDict


class DevicesRequest(SdkBaseModel):
    """Request body for retrieving devices based on vendorID and optional filters"""

    vendor_id: str = Field(alias="VendorId")
    """The ID the vendor wants its devices to be registered under. E.g. Verizon, GM, Ford, etc."""

    filter: Optional[Filter] = Field(default=UNSET, alias="Filter")
    """Devices filter criteria or pagination token"""


class DevicesRequestDict(TypedDict):
    vendor_id: str
    filter: NotRequired[Filter | FilterDict]
