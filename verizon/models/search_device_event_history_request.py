from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .account_identifier import AccountIdentifier, AccountIdentifierDict
from .resource_identifier import ResourceIdentifier, ResourceIdentifierDict


class SearchDeviceEventHistoryRequest(SdkBaseModel):
    """Search Device By Property resource definition."""

    accountidentifier: AccountIdentifier
    """The ID of the authenticating billing account, in the format ``{"billingaccountid":"1234567890-12345"}``."""

    selection: Optional[dict[str, str]] = Field(default=UNSET, alias="$selection")
    """A comma-separated list of properties and comparator values to match against subscriptions in the ThingSpace
    account. See Working with Query Filters for more information. If the request does not include ``$selection``, the
    response will include all subscriptions to which the requesting user has access."""

    resourceidentifier: ResourceIdentifier
    """The ID of the target to delete, in the format {"id": "dd1682d3-2d80-cefc-f3ee-25154800beff"}."""

    limitnumber: Optional[int] = Field(default=UNSET, alias="$limitnumber")
    """The maximum number of events to include in the response."""

    page: Optional[str] = Field(default=UNSET, alias="$page")
    """The maximum number of events to include in the response."""


class SearchDeviceEventHistoryRequestDict(TypedDict):
    accountidentifier: AccountIdentifier | AccountIdentifierDict
    selection: NotRequired[dict[str, str]]
    resourceidentifier: ResourceIdentifier | ResourceIdentifierDict
    limitnumber: NotRequired[int]
    page: NotRequired[str]
