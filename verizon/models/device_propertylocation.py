from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class DevicePropertylocation(SdkBaseModel):
    latitude: Optional[str] = UNSET
    longitude: Optional[str] = UNSET


class DevicePropertylocationDict(TypedDict):
    latitude: NotRequired[str]
    longitude: NotRequired[str]
