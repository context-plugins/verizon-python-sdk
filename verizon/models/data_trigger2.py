from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .actionobject import Actionobject, ActionobjectDict
from .allowance_threshold import AllowanceThreshold, AllowanceThresholdDict
from .device_group_filter_criteria import DeviceGroupFilterCriteria, DeviceGroupFilterCriteriaDict
from .enums.comparitor import ComparitorOrStr
from .enums.condition_type import ConditionTypeOrStr
from .enums.rules_cycle_type import RulesCycleTypeOrStr
from .enums.threshold_unit import ThresholdUnitOrStr


class DataTrigger2(SdkBaseModel):
    device_group: Optional[DeviceGroupFilterCriteria] = Field(default=UNSET, alias="deviceGroup")
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
    action: Optional[Actionobject] = UNSET


class DataTrigger2Dict(TypedDict):
    device_group: NotRequired[DeviceGroupFilterCriteria | DeviceGroupFilterCriteriaDict]
    condition_type: NotRequired[ConditionTypeOrStr]
    comparitor: NotRequired[ComparitorOrStr]
    threshold: NotRequired[int]
    threshold_unit: NotRequired[ThresholdUnitOrStr]
    cycle_type: NotRequired[RulesCycleTypeOrStr]
    allowance_threshold: NotRequired[AllowanceThreshold | AllowanceThresholdDict]
    action: NotRequired[Actionobject | ActionobjectDict]
