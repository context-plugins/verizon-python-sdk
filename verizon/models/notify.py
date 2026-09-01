from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .unions.account_group_share_threshold import AccountGroupShareThreshold, AccountGroupShareThresholdDict


class Notify(SdkBaseModel):
    alert_type: Optional[str] = Field(default=UNSET, alias="alertType")
    threshold: Optional[list[AccountGroupShareThreshold]] = UNSET


class NotifyDict(TypedDict):
    alert_type: NotRequired[str]
    threshold: NotRequired[list[AccountGroupShareThreshold | AccountGroupShareThresholdDict]]
