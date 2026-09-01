from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class DeviceLabels(SdkBaseModel):
    """A label for a single device."""

    name: str
    """The label you want to associate with the device."""

    value: str
    """The value of label"""


class DeviceLabelsDict(TypedDict):
    name: str
    value: str
