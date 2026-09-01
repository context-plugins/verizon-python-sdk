from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ESimdeviceId(SdkBaseModel):
    id: Optional[str] = UNSET
    kind: Optional[str] = UNSET


class ESimdeviceIdDict(TypedDict):
    id: NotRequired[str]
    kind: NotRequired[str]
