from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .connection_event import ConnectionEvent, ConnectionEventDict


class ConnectionHistoryResult(SdkBaseModel):
    """Response containing the connection history. It is a list of Network Connection Events for a device."""

    connection_history: Optional[list[ConnectionEvent]] = Field(default=UNSET, alias="connectionHistory")
    """Device connection events, sorted by the occurredAt timestamp, oldest first."""

    has_more_data: Optional[bool] = Field(default=UNSET, alias="hasMoreData")
    """False for a status 200 response.True for a status 202 response, indicating that there is more data to be
    retrieved. Send another request, adjusting the earliest value in the request based on the occuredAt value for the
    last device in the current response."""


class ConnectionHistoryResultDict(TypedDict):
    connection_history: NotRequired[list[ConnectionEvent | ConnectionEventDict]]
    has_more_data: NotRequired[bool]
