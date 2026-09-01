from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .engagement import Engagement, EngagementDict


class AccountStatesAndServices(SdkBaseModel):
    """Returns a list and details of all custom services and states defined for a specified account."""

    engagement: list[Engagement]
    """The engagements associated with the account."""


class AccountStatesAndServicesDict(TypedDict):
    engagement: list[Engagement | EngagementDict]
