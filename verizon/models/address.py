from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Address(SdkBaseModel):
    """The customer address for the line's primary place of use, for line usage taxation."""

    address_line1: str = Field(alias="addressLine1")
    """The street address for the line's primary place of use. This must be a physical address for taxation; it cannot
    be a P.O. box."""

    address_line2: Optional[str] = Field(default=UNSET, alias="addressLine2")
    """Optional additional street address information."""

    city: str
    """The city for the line's primary place of use."""

    state: str
    """The state for the line's primary place of use."""

    zip: str
    """The ZIP code for the line's primary place of use."""

    zip4: Optional[str] = UNSET
    """The ZIP+4 for the line's primary place of use."""

    country: str
    """Either “US” or “USA” for the country of the line's primary place of use."""

    phone: Optional[str] = UNSET
    """A phone number where the customer can be reached."""

    phone_type: Optional[str] = Field(default=UNSET, alias="phoneType")
    """A single letter to indicate the customer phone type."""

    email_address: Optional[str] = Field(default=UNSET, alias="emailAddress")
    """An email address for the customer."""


class AddressDict(TypedDict):
    address_line1: str
    address_line2: NotRequired[str]
    city: str
    state: str
    zip: str
    zip4: NotRequired[str]
    country: str
    phone: NotRequired[str]
    phone_type: NotRequired[str]
    email_address: NotRequired[str]
