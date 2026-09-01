from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class DropResponseItem(SdkBaseModel):
    imei: Optional[str] = UNSET


class DropResponseItemDict(TypedDict):
    imei: NotRequired[str]
