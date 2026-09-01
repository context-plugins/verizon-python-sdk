from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .address_item import AddressItem, AddressItemDict


class Locations(SdkBaseModel):
    """Location details."""

    address_list: Optional[list[AddressItem]] = Field(default=UNSET, alias="addressList")


class LocationsDict(TypedDict):
    address_list: NotRequired[list[AddressItem | AddressItemDict]]
