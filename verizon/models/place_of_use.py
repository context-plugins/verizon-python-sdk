from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .address import Address, AddressDict
from .customer_name import CustomerName, CustomerNameDict


class PlaceOfUse(SdkBaseModel):
    """The customer name and the address of the device's primary place of use. Leave these fields empty to use the
    account profile address as the primary place of use. These values will be applied to all devices in the request.If
    the account is enabled for non-geographic MDNs and the device supports it, the primaryPlaceOfUse address will also
    be used to derive the MDN for the device."""

    address: Address
    """The customer address for the line's primary place of use, for line usage taxation."""

    customer_name: CustomerName = Field(alias="customerName")
    """The customer name to be used for line usage taxation."""


class PlaceOfUseDict(TypedDict):
    address: Address | AddressDict
    customer_name: CustomerName | CustomerNameDict
