from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .security_subscription import SecuritySubscription, SecuritySubscriptionDict


class SecuritySubscriptionResult(SdkBaseModel):
    """Response for a subscription request."""

    account_name: Optional[str] = Field(default=UNSET, alias="accountName")
    """The name of a billing account."""

    subscription_list: Optional[list[SecuritySubscription]] = Field(default=UNSET, alias="subscriptionList")
    """The list of SKU numbers and counts for each license type specified in the request."""


class SecuritySubscriptionResultDict(TypedDict):
    account_name: NotRequired[str]
    subscription_list: NotRequired[list[SecuritySubscription | SecuritySubscriptionDict]]
