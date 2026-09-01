from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class QosdeviceId(SdkBaseModel):
    id: Optional[str] = UNSET
    kind: Optional[str] = UNSET


class QosdeviceIdDict(TypedDict):
    id: NotRequired[str]
    kind: NotRequired[str]
