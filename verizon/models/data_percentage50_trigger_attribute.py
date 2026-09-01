from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class DataPercentage50TriggerAttribute(SdkBaseModel):
    """Trigger attribute for when data percentage is over 50% used."""

    key: Optional[str] = UNSET
    """Key data percentage 50."""

    value: Optional[bool] = UNSET
    """DataPercentage50<br />True - Trigger on Data percentage is over 50% used<br />False - Do not trigger when over
    50% used."""


class DataPercentage50TriggerAttributeDict(TypedDict):
    key: NotRequired[str]
    value: NotRequired[bool]
