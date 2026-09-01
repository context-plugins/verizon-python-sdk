from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ActiveTriggerIndicator(SdkBaseModel):
    """Whether the trigger is active or not."""

    active: Optional[bool] = UNSET
    """Indicates if the trigger is active<br />True - trigger is active<br />False - trigger is not active."""


class ActiveTriggerIndicatorDict(TypedDict):
    active: NotRequired[bool]
