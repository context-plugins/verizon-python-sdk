from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .device_group_filter_criteria import DeviceGroupFilterCriteria, DeviceGroupFilterCriteriaDict


class DeviceGroupObject(SdkBaseModel):
    device_group: Optional[DeviceGroupFilterCriteria] = Field(default=UNSET, alias="deviceGroup")


class DeviceGroupObjectDict(TypedDict):
    device_group: NotRequired[DeviceGroupFilterCriteria | DeviceGroupFilterCriteriaDict]
