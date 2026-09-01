from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class SessionTriggerRequest(SdkBaseModel):
    comparator: Optional[str] = UNSET
    threshold: Optional[int] = UNSET


class SessionTriggerRequestDict(TypedDict):
    comparator: NotRequired[str]
    threshold: NotRequired[int]
