from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class NoOfDaysB4PromoExp(SdkBaseModel):
    key: Optional[str] = UNSET
    value: Optional[int] = UNSET


class NoOfDaysB4PromoExpDict(TypedDict):
    key: NotRequired[str]
    value: NotRequired[int]
