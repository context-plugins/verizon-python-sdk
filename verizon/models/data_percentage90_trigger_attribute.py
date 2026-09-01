from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class DataPercentage90TriggerAttribute(SdkBaseModel):
    """Trigger attribute for when data percentage is over 90% used."""

    key: Optional[str] = UNSET
    """Key data percentage 90."""

    value: Optional[bool] = UNSET
    """DataPercentage90<br />True - Trigger on Data percentage is over 90% used<br />False - Do not trigger when over
    90% used."""


class DataPercentage90TriggerAttributeDict(TypedDict):
    key: NotRequired[str]
    value: NotRequired[bool]
