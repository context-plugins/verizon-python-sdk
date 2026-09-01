from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .address import Address, AddressDict


class Addressquery(SdkBaseModel):
    address: Optional[list[Address]] = UNSET


class AddressqueryDict(TypedDict):
    address: NotRequired[list[Address | AddressDict]]
