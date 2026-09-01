from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class HplDeviceId(SdkBaseModel):
    """Identifier object pairs of kind/id"""

    kind: Optional[str] = UNSET
    """The type of ID. This can be IMEI or ICCID."""

    id: Optional[str] = UNSET
    """The ID value."""


class HplDeviceIdDict(TypedDict):
    kind: NotRequired[str]
    id: NotRequired[str]
