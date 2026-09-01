from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class V1DeviceListItem(SdkBaseModel):
    """A JSON object for each device that was included in the request, showing the device IMEI, the status of the
    addition or removal, and additional information about the status."""

    device_id: Optional[str] = Field(default=UNSET, alias="deviceId")
    """Device IMEI."""

    status: Optional[str] = UNSET
    """Whether the device was successfully added or removed from the campaign."""

    reason: Optional[str] = Field(default=UNSET, alias="Reason")
    """Additional details about the status."""


class V1DeviceListItemDict(TypedDict):
    device_id: NotRequired[str]
    status: NotRequired[str]
    reason: NotRequired[str]
