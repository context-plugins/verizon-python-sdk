from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .giodevice_id import GiodeviceId, GiodeviceIdDict


class AggregateUsage(SdkBaseModel):
    device_id: Optional[GiodeviceId] = Field(default=UNSET, alias="deviceId")
    account_name: Optional[str] = Field(default=UNSET, alias="accountName")
    """The numeric name of the account, in the format "0000123456-00001". Leading zeros must be included."""

    start_time: Optional[str] = Field(default=UNSET, alias="startTime")
    """The start date of the time period queried as "$datetime"
    """

    end_time: Optional[str] = Field(default=UNSET, alias="endTime")
    """The end date of the time period being queried as "$datetime"
    """


class AggregateUsageDict(TypedDict):
    device_id: NotRequired[GiodeviceId | GiodeviceIdDict]
    account_name: NotRequired[str]
    start_time: NotRequired[str]
    end_time: NotRequired[str]
