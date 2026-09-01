from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Gbiattribute15(SdkBaseModel):
    key: Optional[str] = UNSET


class Gbiattribute15Dict(TypedDict):
    key: NotRequired[str]
