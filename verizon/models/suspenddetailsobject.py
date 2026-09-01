from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.threshold_unit import ThresholdUnitOrStr


class Suspenddetailsobject(SdkBaseModel):
    suspend_from_accounts: Optional[list[str]] = Field(default=UNSET, alias="suspendFromAccounts")
    suspend_duration: Optional[int] = Field(default=UNSET, alias="suspendDuration")
    suspend_option: Optional[str] = Field(default=UNSET, alias="suspendOption")
    threshold: Optional[int] = UNSET
    """The threshold value the trigger monitors for"""

    threshold_unit: Optional[ThresholdUnitOrStr] = Field(default=UNSET, alias="thresholdUnit")
    """The units of the threshold. This can be KB, Kilobits, MB, Megabits, or GB, Gigabits"""


class SuspenddetailsobjectDict(TypedDict):
    suspend_from_accounts: NotRequired[list[str]]
    suspend_duration: NotRequired[int]
    suspend_option: NotRequired[str]
    threshold: NotRequired[int]
    threshold_unit: NotRequired[ThresholdUnitOrStr]
