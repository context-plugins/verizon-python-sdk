from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class DataPercentage100TriggerAttribute(SdkBaseModel):
    """Trigger attribute for when data percentage is over 100% used."""

    key: Optional[str] = UNSET
    """Key data percentage 100."""

    value: Optional[bool] = UNSET
    """DataPercentage100<br />True - Trigger on Data percentage is over 100% used<br />False - Do not trigger when over
    100% used."""


class DataPercentage100TriggerAttributeDict(TypedDict):
    key: NotRequired[str]
    value: NotRequired[bool]
