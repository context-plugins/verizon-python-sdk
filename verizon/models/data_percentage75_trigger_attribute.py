from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class DataPercentage75TriggerAttribute(SdkBaseModel):
    """Trigger attribute for when data percentage is over 75% used."""

    key: Optional[str] = UNSET
    """Key data percentage 75."""

    value: Optional[bool] = UNSET
    """DataPercentage75<br />True - Trigger on Data percentage is over 75% used<br />False - Do not trigger when over
    75% used."""


class DataPercentage75TriggerAttributeDict(TypedDict):
    key: NotRequired[str]
    value: NotRequired[bool]
