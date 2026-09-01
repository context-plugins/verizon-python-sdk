from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class V3DeviceListItem(SdkBaseModel):
    """Device changed."""

    device_id: Optional[str] = Field(default=UNSET, alias="deviceId")
    """Device IMEI."""

    status: Optional[str] = UNSET
    """Success or failure."""

    reason: Optional[str] = Field(default=UNSET, alias="Reason")
    """Result reason."""


class V3DeviceListItemDict(TypedDict):
    device_id: NotRequired[str]
    status: NotRequired[str]
    reason: NotRequired[str]
