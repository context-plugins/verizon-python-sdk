from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .unions.triggers_list_options import TriggersListOptions, TriggersListOptionsDict


class AnomalyTriggerResult(SdkBaseModel):
    """A result containing a list of anomaly triggers."""

    triggers: Optional[list[TriggersListOptions]] = UNSET
    """Trigger value chunk details."""


class AnomalyTriggerResultDict(TypedDict):
    triggers: NotRequired[list[TriggersListOptions | TriggersListOptionsDict]]
