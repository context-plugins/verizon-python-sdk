from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class DeviceIdentifier(SdkBaseModel):
    """Device Id details."""

    kind: str
    """Kind of device."""

    id: str
    """Device Identity number."""

    mdn: Optional[str] = UNSET
    """Device MDN number."""


class DeviceIdentifierDict(TypedDict):
    kind: str
    id: str
    mdn: NotRequired[str]
