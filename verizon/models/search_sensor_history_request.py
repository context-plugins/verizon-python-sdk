from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .account_identifier import AccountIdentifier, AccountIdentifierDict
from .resource_identifier import ResourceIdentifier, ResourceIdentifierDict


class SearchSensorHistoryRequest(SdkBaseModel):
    """Search Device By Property resource definition."""

    accountidentifier: AccountIdentifier
    """The ID of the authenticating billing account, in the format ``{"billingaccountid":"1234567890-12345"}``."""

    resourceidentifier: ResourceIdentifier
    """The ID of the target to delete, in the format {"id": "dd1682d3-2d80-cefc-f3ee-25154800beff"}."""

    limitnumber: Optional[int] = Field(default=UNSET, alias="$limitnumber")
    """The maximum number of events to include in the response."""

    page: Optional[str] = Field(default=UNSET, alias="$page")
    """The maximum number of events to include in the response."""


class SearchSensorHistoryRequestDict(TypedDict):
    accountidentifier: AccountIdentifier | AccountIdentifierDict
    resourceidentifier: ResourceIdentifier | ResourceIdentifierDict
    limitnumber: NotRequired[int]
    page: NotRequired[str]
