from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .account_service import AccountService, AccountServiceDict


class Engagement(SdkBaseModel):
    """The engagements associated with the account."""

    engagement_id: Optional[str] = Field(default=UNSET, alias="engagementId")
    """The engagement ID."""

    charging_group: Optional[str] = Field(default=UNSET, alias="chargingGroup")
    """The charging group name."""

    services: Optional[list[AccountService]] = UNSET
    """The services associated with the account."""


class EngagementDict(TypedDict):
    engagement_id: NotRequired[str]
    charging_group: NotRequired[str]
    services: NotRequired[list[AccountService | AccountServiceDict]]
