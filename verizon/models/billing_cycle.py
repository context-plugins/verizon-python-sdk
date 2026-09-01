from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class BillingCycle(SdkBaseModel):
    year: Optional[str] = UNSET
    month: Optional[str] = UNSET


class BillingCycleDict(TypedDict):
    year: NotRequired[str]
    month: NotRequired[str]
