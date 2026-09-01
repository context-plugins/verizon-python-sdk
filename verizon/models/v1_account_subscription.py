from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class V1AccountSubscription(SdkBaseModel):
    """Account subscription information."""

    account_name: Optional[str] = Field(default=UNSET, alias="accountName")
    """Account identifier in "##########-#####"."""

    purchase_type: Optional[str] = Field(default=UNSET, alias="purchaseType")
    """Subscription models used by the account."""

    license_count: Optional[int] = Field(default=UNSET, alias="licenseCount")
    """Number of monthly licenses in an MRC subscription."""

    license_used_count: Optional[int] = Field(default=UNSET, alias="licenseUsedCount")
    """Number of licenses currently assigned to devices."""

    update_time: Optional[str] = Field(default=UNSET, alias="updateTime")
    """The date and time of when the subscription was last updated."""


class V1AccountSubscriptionDict(TypedDict):
    account_name: NotRequired[str]
    purchase_type: NotRequired[str]
    license_count: NotRequired[int]
    license_used_count: NotRequired[int]
    update_time: NotRequired[str]
