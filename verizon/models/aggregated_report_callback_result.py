from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.aggregated_report_callback_status import AggregatedReportCallbackStatusOrStr


class AggregatedReportCallbackResult(SdkBaseModel):
    """Aggregated usage report (Asynchronous)."""

    txid: Optional[str] = UNSET
    """A unique string (UUID) that associates the request with the location report information that is sent in
    asynchronous callback message.ThingSpace will send a separate callback message for each device that was in the
    request. All of the callback messages will have a txid."""

    status: Optional[AggregatedReportCallbackStatusOrStr] = UNSET
    """QUEUED or COMPLETED. Requests for IoT devices with cacheMode=0 (cached) have status=COMPLETED; all other requests
    are QUEUED."""


class AggregatedReportCallbackResultDict(TypedDict):
    txid: NotRequired[str]
    status: NotRequired[AggregatedReportCallbackStatusOrStr]
