from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class V2DeviceStatus(SdkBaseModel):
    """Device with id in IMEI."""

    device_id: str = Field(alias="deviceId")
    """Device IMEI."""

    status: str
    """Success or failure."""

    result_reason: Optional[str] = Field(default=UNSET, alias="resultReason")
    """Result reason."""


class V2DeviceStatusDict(TypedDict):
    device_id: str
    status: str
    result_reason: NotRequired[str]
