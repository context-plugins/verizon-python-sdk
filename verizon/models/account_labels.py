from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .device_labels import DeviceLabels, DeviceLabelsDict
from .device_list import DeviceList, DeviceListDict


class AccountLabels(SdkBaseModel):
    """Maximum of 2,000 objects are allowed in the array."""

    devices: list[DeviceList]
    label: Optional[list[DeviceLabels]] = UNSET


class AccountLabelsDict(TypedDict):
    devices: list[DeviceList | DeviceListDict]
    label: NotRequired[list[DeviceLabels | DeviceLabelsDict]]
