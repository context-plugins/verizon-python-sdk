from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .device_id import DeviceId, DeviceIdDict
from .label import Label, LabelDict


class DeviceUsageListRequest(SdkBaseModel):
    """Request to return the daily network data usage of a single device during a specified time period."""

    earliest: str
    """The earliest date for which you want usage data."""

    latest: str
    """The last date for which you want usage data."""

    device_id: Optional[DeviceId] = Field(default=UNSET, alias="deviceId")
    """An identifier for a single device."""

    label: Optional[Label] = UNSET


class DeviceUsageListRequestDict(TypedDict):
    earliest: str
    latest: str
    device_id: NotRequired[DeviceId | DeviceIdDict]
    label: NotRequired[Label | LabelDict]
