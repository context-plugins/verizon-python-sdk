from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .triggervalues2 import Triggervalues2, Triggervalues2Dict


class TriggerValueResponse2(SdkBaseModel):
    triggers: Optional[list[Triggervalues2]] = UNSET


class TriggerValueResponse2Dict(TypedDict):
    triggers: NotRequired[list[Triggervalues2 | Triggervalues2Dict]]
