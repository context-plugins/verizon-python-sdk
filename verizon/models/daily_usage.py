from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .giodevice_id import GiodeviceId, GiodeviceIdDict


class DailyUsage(SdkBaseModel):
    device_id: Optional[GiodeviceId] = Field(default=UNSET, alias="deviceId")
    earliest: Optional[str] = UNSET
    """The start date of the time period queried as "$datetime"
    """

    latest: Optional[str] = UNSET
    """The end date of the time period being queried as "$datetime"
    """


class DailyUsageDict(TypedDict):
    device_id: NotRequired[GiodeviceId | GiodeviceIdDict]
    earliest: NotRequired[str]
    latest: NotRequired[str]
