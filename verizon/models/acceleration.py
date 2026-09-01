from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Acceleration(SdkBaseModel):
    x: Optional[str] = UNSET
    y: Optional[str] = UNSET
    z: Optional[str] = UNSET


class AccelerationDict(TypedDict):
    x: NotRequired[str]
    y: NotRequired[str]
    z: NotRequired[str]
