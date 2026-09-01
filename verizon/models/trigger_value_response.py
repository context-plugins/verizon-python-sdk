from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .triggervalues import Triggervalues, TriggervaluesDict


class TriggerValueResponse(SdkBaseModel):
    triggers: Optional[list[Triggervalues]] = UNSET


class TriggerValueResponseDict(TypedDict):
    triggers: NotRequired[list[Triggervalues | TriggervaluesDict]]
