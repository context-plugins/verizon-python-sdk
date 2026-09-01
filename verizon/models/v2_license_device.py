from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class V2LicenseDevice(SdkBaseModel):
    """Device IMEI list."""

    device_id: str = Field(alias="deviceId")
    """Device IMEI."""

    assignment_time: Optional[str] = Field(default=UNSET, alias="assignmentTime")
    """License assignment time."""


class V2LicenseDeviceDict(TypedDict):
    device_id: str
    assignment_time: NotRequired[str]
