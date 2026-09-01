from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.condition_action import ConditionActionOrStr


class AccountGroupShareCondition(SdkBaseModel):
    action: Optional[ConditionActionOrStr] = UNSET
    """The action taken when trigger conditions are met"""


class AccountGroupShareConditionDict(TypedDict):
    action: NotRequired[ConditionActionOrStr]
