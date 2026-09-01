from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class AddressItem(SdkBaseModel):
    """Address details."""

    address_line1: Optional[str] = Field(default=UNSET, alias="addressLine1")
    """Street Address."""

    address_line2: Optional[str] = Field(default=UNSET, alias="addressLine2")
    """Optional address information."""

    city: Optional[str] = UNSET
    """Name of the city."""

    state: Optional[str] = UNSET
    """State code."""

    country: Optional[str] = UNSET
    """Country."""

    zip: Optional[str] = UNSET
    """Five digit zipcode."""

    zip4: Optional[str] = UNSET
    """Four digit zip code."""


class AddressItemDict(TypedDict):
    address_line1: NotRequired[str]
    address_line2: NotRequired[str]
    city: NotRequired[str]
    state: NotRequired[str]
    country: NotRequired[str]
    zip: NotRequired[str]
    zip4: NotRequired[str]
