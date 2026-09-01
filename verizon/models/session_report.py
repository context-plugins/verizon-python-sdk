from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .daily_usage_item import DailyUsageItem, DailyUsageItemDict


class SessionReport(SdkBaseModel):
    """Session report for a device."""

    id: str
    """The 10-digit ID of the device."""

    txid: str
    """A unique string (UUID) that associates the request with the location report information that is sent in
    asynchronous callback message.ThingSpace will send a separate callback message for each device that was in the
    request. All of the callback messages will have a txid."""

    sessions: Optional[list[DailyUsageItem]] = UNSET
    """An object containing the start and end time of the session with the amount of data transferred."""


class SessionReportDict(TypedDict):
    id: str
    txid: str
    sessions: NotRequired[list[DailyUsageItem | DailyUsageItemDict]]
