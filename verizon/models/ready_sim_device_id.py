from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ReadySimDeviceId(SdkBaseModel):
    kind: Optional[str] = UNSET
    id: Optional[str] = UNSET


class ReadySimDeviceIdDict(TypedDict):
    kind: NotRequired[str]
    id: NotRequired[str]
