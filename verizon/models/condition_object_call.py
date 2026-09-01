from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .allowance_threshold import AllowanceThreshold, AllowanceThresholdDict
from .enums.comparitor import ComparitorOrStr
from .enums.condition_type import ConditionTypeOrStr
from .enums.rules_cycle_type import RulesCycleTypeOrStr
from .enums.threshold_unit import ThresholdUnitOrStr


class ConditionObjectCall(SdkBaseModel):
    condition_type: Optional[ConditionTypeOrStr] = Field(default=UNSET, alias="conditionType")
    """The condition type being monitored"""

    comparitor: Optional[ComparitorOrStr] = UNSET
    """The boolean of the comparison. ``gt`` is Greater Than, ``lt`` is Less Than and ``eq`` is Equal To"""

    threshold: Optional[int] = UNSET
    """The threshold value the trigger monitors for"""

    threshold_unit: Optional[ThresholdUnitOrStr] = Field(default=UNSET, alias="thresholdUnit")
    """The units of the threshold. This can be KB, Kilobits, MB, Megabits, or GB, Gigabits"""

    cycle_type: Optional[RulesCycleTypeOrStr] = Field(default=UNSET, alias="cycleType")
    """The interval to monitor for the threshold. This can be Daily, Weekly or Monthly"""

    allowance_threshold: Optional[AllowanceThreshold] = Field(default=UNSET, alias="allowanceThreshold")


class ConditionObjectCallDict(TypedDict):
    condition_type: NotRequired[ConditionTypeOrStr]
    comparitor: NotRequired[ComparitorOrStr]
    threshold: NotRequired[int]
    threshold_unit: NotRequired[ThresholdUnitOrStr]
    cycle_type: NotRequired[RulesCycleTypeOrStr]
    allowance_threshold: NotRequired[AllowanceThreshold | AllowanceThresholdDict]
