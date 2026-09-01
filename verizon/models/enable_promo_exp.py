from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class EnablePromoExp(SdkBaseModel):
    key: Optional[str] = UNSET
    value: Optional[bool] = UNSET


class EnablePromoExpDict(TypedDict):
    key: NotRequired[str]
    value: NotRequired[bool]
