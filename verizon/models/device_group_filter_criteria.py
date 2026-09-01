from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .device_group_filter import DeviceGroupFilter, DeviceGroupFilterDict


class DeviceGroupFilterCriteria(SdkBaseModel):
    filter_criteria: Optional[DeviceGroupFilter] = Field(default=UNSET, alias="filterCriteria")


class DeviceGroupFilterCriteriaDict(TypedDict):
    filter_criteria: NotRequired[DeviceGroupFilter | DeviceGroupFilterDict]
