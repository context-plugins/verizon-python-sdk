from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .data_trigger1 import DataTrigger1, DataTrigger1Dict
from .enums.trigger_category import TriggerCategoryOrStr
from .notificationarray import Notificationarray, NotificationarrayDict


class AccountLevelUpdateTrigger(SdkBaseModel):
    trigger_id: Optional[str] = Field(default=UNSET, alias="triggerId")
    """The system assigned UUID of the trigger"""

    trigger_name: Optional[str] = Field(default=UNSET, alias="triggerName")
    """The user defined name of the trigger"""

    ecpd_id: Optional[str] = Field(default=UNSET, alias="ecpdId")
    """The Enterprise Customer Profile Database ID"""

    trigger_category: Optional[TriggerCategoryOrStr] = Field(default=UNSET, alias="triggerCategory")
    """The type of trigger being created or modified"""

    data_trigger: Optional[DataTrigger1] = Field(default=UNSET, alias="dataTrigger")
    notification: Optional[Notificationarray] = UNSET


class AccountLevelUpdateTriggerDict(TypedDict):
    trigger_id: NotRequired[str]
    trigger_name: NotRequired[str]
    ecpd_id: NotRequired[str]
    trigger_category: NotRequired[TriggerCategoryOrStr]
    data_trigger: NotRequired[DataTrigger1 | DataTrigger1Dict]
    notification: NotRequired[Notificationarray | NotificationarrayDict]
