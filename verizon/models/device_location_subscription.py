from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class DeviceLocationSubscription(SdkBaseModel):
    account_name: Optional[str] = Field(default=UNSET, alias="accountName")
    """Account identifier in "##########-#####"."""

    loc_type: Optional[str] = Field(default=UNSET, alias="locType")
    """Location service license type."""

    max_allowance: Optional[str] = Field(default=UNSET, alias="maxAllowance")
    """The number of billable location requests allowed per billing cycle."""

    purchase_time: Optional[str] = Field(default=UNSET, alias="purchaseTime")
    """Location service purchase time."""


class DeviceLocationSubscriptionDict(TypedDict):
    account_name: NotRequired[str]
    loc_type: NotRequired[str]
    max_allowance: NotRequired[str]
    purchase_time: NotRequired[str]
