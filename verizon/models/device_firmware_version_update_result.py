from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class DeviceFirmwareVersionUpdateResult(SdkBaseModel):
    """Device firmware version update response."""

    account_name: str = Field(alias="accountName")
    """Account identifier."""

    request_id: str = Field(alias="requestId")
    """Request identifier."""


class DeviceFirmwareVersionUpdateResultDict(TypedDict):
    account_name: str
    request_id: str
