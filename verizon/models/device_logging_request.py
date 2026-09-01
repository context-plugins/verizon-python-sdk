from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class DeviceLoggingRequest(SdkBaseModel):
    """Device logging information."""

    device_ids: list[str] = Field(alias="deviceIds")
    """List of device IMEI identifiers."""


class DeviceLoggingRequestDict(TypedDict):
    device_ids: list[str]
