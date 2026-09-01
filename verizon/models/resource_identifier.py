from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ResourceIdentifier(SdkBaseModel):
    """The ID of the target to delete, in the format {"id": "dd1682d3-2d80-cefc-f3ee-25154800beff"}."""

    id: Optional[str] = UNSET
    """Target ID."""

    imei: Optional[str] = UNSET
    """Device IMEI."""


class ResourceIdentifierDict(TypedDict):
    id: NotRequired[str]
    imei: NotRequired[str]
