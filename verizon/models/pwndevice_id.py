from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class PwndeviceId(SdkBaseModel):
    id: str
    kind: str


class PwndeviceIdDict(TypedDict):
    id: str
    kind: str
