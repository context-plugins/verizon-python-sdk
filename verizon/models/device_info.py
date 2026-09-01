from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class DeviceInfo(SdkBaseModel):
    """The devices that you want to locate. The array cannot contain more than 20 devices."""

    id: str
    """Device identifier."""

    kind: str
    """Device identifier kind."""

    mdn: str
    """Device MDN."""


class DeviceInfoDict(TypedDict):
    id: str
    kind: str
    mdn: str
