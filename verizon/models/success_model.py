from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class SuccessModel(SdkBaseModel):
    status: Optional[str] = UNSET


class SuccessModelDict(TypedDict):
    status: NotRequired[str]
