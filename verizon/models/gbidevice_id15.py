from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class GbideviceId15(SdkBaseModel):
    id: Optional[str] = UNSET
    kind: Optional[str] = UNSET


class GbideviceId15Dict(TypedDict):
    id: NotRequired[str]
    kind: NotRequired[str]
