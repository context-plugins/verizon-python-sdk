from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class GiodeviceId(SdkBaseModel):
    kind: str
    id: str


class GiodeviceIdDict(TypedDict):
    kind: str
    id: str
