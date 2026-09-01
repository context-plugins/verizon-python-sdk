from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Device(SdkBaseModel):
    """Identifies a particular IoT device."""

    id: str
    """Device identifier."""

    kind: str
    """Device kind identifier."""


class DeviceDict(TypedDict):
    id: str
    kind: str
