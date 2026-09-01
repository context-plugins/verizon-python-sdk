from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .account_level_filter import AccountLevelFilter, AccountLevelFilterDict
from .allowance_threshold import AllowanceThreshold, AllowanceThresholdDict
from .enums.account_level_action import AccountLevelActionOrStr
from .enums.comparitor import ComparitorOrStr
from .enums.condition_type import ConditionTypeOrStr
from .enums.rules_cycle_type import RulesCycleTypeOrStr
from .enums.threshold_unit import ThresholdUnitOrStr
from .unions.account_level_objectcondition import AccountLevelObjectcondition, AccountLevelObjectconditionDict


class DataTrigger1(SdkBaseModel):
    filter_criteria: Optional[AccountLevelFilter] = Field(default=UNSET, alias="filterCriteria")
    condition: Optional[AccountLevelObjectcondition] = UNSET
    action: Optional[AccountLevelActionOrStr] = UNSET
    """The action taken when trigger conditions are met"""

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


class DataTrigger1Dict(TypedDict):
    filter_criteria: NotRequired[AccountLevelFilter | AccountLevelFilterDict]
    condition: NotRequired[AccountLevelObjectcondition | AccountLevelObjectconditionDict]
    action: NotRequired[AccountLevelActionOrStr]
    condition_type: NotRequired[ConditionTypeOrStr]
    comparitor: NotRequired[ComparitorOrStr]
    threshold: NotRequired[int]
    threshold_unit: NotRequired[ThresholdUnitOrStr]
    cycle_type: NotRequired[RulesCycleTypeOrStr]
    allowance_threshold: NotRequired[AllowanceThreshold | AllowanceThresholdDict]
