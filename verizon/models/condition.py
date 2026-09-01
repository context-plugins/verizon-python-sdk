from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .keyschunk2 import Keyschunk2, Keyschunk2Dict


class Condition(SdkBaseModel):
    condition: Optional[list[Keyschunk2]] = UNSET


class ConditionDict(TypedDict):
    condition: NotRequired[list[Keyschunk2 | Keyschunk2Dict]]
