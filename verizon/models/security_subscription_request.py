from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class SecuritySubscriptionRequest(SdkBaseModel):
    """Request for a subscription."""

    account_name: Optional[str] = Field(default=UNSET, alias="accountName")
    """The name of a billing account."""

    sku_number: Optional[str] = Field(default=UNSET, alias="skuNumber")
    """The Stock Keeping Unit (SKU). Valid skuNumbers for SIM-Secure for IoT are:SIMSec-IoT-Lt”. (Lifetime) Once a
    license is assigned to a SIM, the SIM-Secure feature is enabled for the life of the SIM.“TS-BUNDLE-KTO-SIMSEC-MRC”.
    (Bundle) The SIM-Secure Flex license can be assigned to or removed from a SIM at any time. This SKU is bundled with
    other ThingSpace Services.*“SIMSec-IoT”. (Flex) The SIM-Secure Flex license can be assigned to or removed from a SIM
    at any time. This SKU is purchased a la carte."""


class SecuritySubscriptionRequestDict(TypedDict):
    account_name: NotRequired[str]
    sku_number: NotRequired[str]
