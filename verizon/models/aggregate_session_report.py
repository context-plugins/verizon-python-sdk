from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .aggregate_usage_error import AggregateUsageError, AggregateUsageErrorDict
from .aggregate_usage_item import AggregateUsageItem, AggregateUsageItemDict


class AggregateSessionReport(SdkBaseModel):
    """Session and usage details for up to 10 devices."""

    txid: Optional[str] = UNSET
    """A unique string (UUID) that associates the request with the location report information that is sent in
    asynchronous callback message.ThingSpace will send a separate callback message for each device that was in the
    request. All of the callback messages will have a txid."""

    usage: Optional[list[AggregateUsageItem]] = UNSET
    """Contains usage per device."""

    errors: Optional[list[AggregateUsageError]] = UNSET
    """An object containing any errors reported by the device."""


class AggregateSessionReportDict(TypedDict):
    txid: NotRequired[str]
    usage: NotRequired[list[AggregateUsageItem | AggregateUsageItemDict]]
    errors: NotRequired[list[AggregateUsageError | AggregateUsageErrorDict]]
