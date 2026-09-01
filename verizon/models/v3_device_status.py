from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel


class V3DeviceStatus(SdkBaseModel):
    """Device status."""

    device_id: str = Field(alias="deviceId")
    """Device IMEI."""

    status: str
    """Success or failure."""

    result_reason: Optional[str] = Field(default=UNSET, alias="resultReason")
    """Result reason."""

    updated_time: Optional[RFC3339DateTime] = Field(default=UNSET, alias="updatedTime")
    """Updated Time."""

    recent_attempt_time: Optional[RFC3339DateTime] = Field(default=UNSET, alias="recentAttemptTime")
    """The most recent attempt time."""

    next_attempt_time: Optional[RFC3339DateTime] = Field(default=UNSET, alias="nextAttemptTime")
    """Next attempt time."""


class V3DeviceStatusDict(TypedDict):
    device_id: str
    status: str
    result_reason: NotRequired[str]
    updated_time: NotRequired[RFC3339DateTime]
    recent_attempt_time: NotRequired[RFC3339DateTime]
    next_attempt_time: NotRequired[RFC3339DateTime]
