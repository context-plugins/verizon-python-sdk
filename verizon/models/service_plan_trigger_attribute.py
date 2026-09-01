from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ServicePlanTriggerAttribute(SdkBaseModel):
    """Key service plan trigger attribute."""

    key: Optional[str] = UNSET
    """The ServicePlan name will be listed here."""


class ServicePlanTriggerAttributeDict(TypedDict):
    key: NotRequired[str]
