from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .device_labels import DeviceLabels, DeviceLabelsDict


class LabelsList(SdkBaseModel):
    device_ids: Optional[list[DeviceLabels]] = Field(default=UNSET, alias="deviceIds")


class LabelsListDict(TypedDict):
    device_ids: NotRequired[list[DeviceLabels | DeviceLabelsDict]]
