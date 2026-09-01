from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .device_id import DeviceId, DeviceIdDict
from .label import Label, LabelDict


class DeviceAggregateUsageListRequest(SdkBaseModel):
    """Request to list device aggregate usage."""

    start_time: str = Field(alias="startTime")
    """The beginning of the reporting period. The startTime cannot be more than 6 months before the current date."""

    end_time: str = Field(alias="endTime")
    """The end of the reporting period. The endTime date must be within on month of the startTime date."""

    device_ids: Optional[list[DeviceId]] = Field(default=UNSET, alias="deviceIds")
    """One or more devices for which you want aggregate data, specified by device ID."""

    account_name: Optional[str] = Field(default=UNSET, alias="accountName")
    """The name of a billing account."""

    group_name: Optional[str] = Field(default=UNSET, alias="groupName")
    """The name of a device group, if you want to only include devices in that group."""

    label: Optional[list[Label]] = UNSET


class DeviceAggregateUsageListRequestDict(TypedDict):
    start_time: str
    end_time: str
    device_ids: NotRequired[list[DeviceId | DeviceIdDict]]
    account_name: NotRequired[str]
    group_name: NotRequired[str]
    label: NotRequired[list[Label | LabelDict]]
