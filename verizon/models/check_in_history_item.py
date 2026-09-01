from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import RFC3339DateTime, SdkBaseModel


class CheckInHistoryItem(SdkBaseModel):
    """Check-in history for a device."""

    device_id: str = Field(alias="deviceId")
    """Device IMEI."""

    client_type: str = Field(alias="clientType")
    """Type of client."""

    result: str
    failure_type: str = Field(alias="failureType")
    time_completed: RFC3339DateTime = Field(alias="timeCompleted")


class CheckInHistoryItemDict(TypedDict):
    device_id: str
    client_type: str
    result: str
    failure_type: str
    time_completed: RFC3339DateTime
