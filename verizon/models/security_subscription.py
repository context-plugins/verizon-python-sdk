from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .extended_attributes import ExtendedAttributes, ExtendedAttributesDict


class SecuritySubscription(SdkBaseModel):
    """Subscription of the device."""

    extended_attributes: Optional[list[ExtendedAttributes]] = Field(default=UNSET, alias="extendedAttributes")
    """Attributes of the subscription."""

    license_assigned: Optional[int] = Field(default=UNSET, alias="licenseAssigned")
    """The total number of licenses for this license type that are assigned to device SIMs."""

    license_available: Optional[int] = Field(default=UNSET, alias="licenseAvailable")
    """The total number of licenses for this license type that are available to assign to device SIMs."""

    license_purchased: Optional[int] = Field(default=UNSET, alias="licensePurchased")
    """The total number of licenses purchased for the license type."""

    license_type: Optional[str] = Field(default=UNSET, alias="licenseType")
    """The license type associated with the skuNumber."""

    sku_number: Optional[str] = Field(default=UNSET, alias="skuNumber")
    """The skuNumber that identifies the license type."""


class SecuritySubscriptionDict(TypedDict):
    extended_attributes: NotRequired[list[ExtendedAttributes | ExtendedAttributesDict]]
    license_assigned: NotRequired[int]
    license_available: NotRequired[int]
    license_purchased: NotRequired[int]
    license_type: NotRequired[str]
    sku_number: NotRequired[str]
