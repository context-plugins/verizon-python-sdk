from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .data_trigger import DataTrigger, DataTriggerDict
from .enums.trigger_category import TriggerCategoryOrStr
from .notificationarray import Notificationarray, NotificationarrayDict


class AccountLevelCreateTrigger(SdkBaseModel):
    trigger_name: Optional[str] = Field(default=UNSET, alias="triggerName")
    """The user defined name of the trigger"""

    ecpd_id: Optional[str] = Field(default=UNSET, alias="ecpdId")
    """The Enterprise Customer Profile Database ID"""

    trigger_category: Optional[TriggerCategoryOrStr] = Field(default=UNSET, alias="triggerCategory")
    """The type of trigger being created or modified"""

    data_trigger: Optional[DataTrigger] = Field(default=UNSET, alias="dataTrigger")
    notification: Optional[Notificationarray] = UNSET


class AccountLevelCreateTriggerDict(TypedDict):
    trigger_name: NotRequired[str]
    ecpd_id: NotRequired[str]
    trigger_category: NotRequired[TriggerCategoryOrStr]
    data_trigger: NotRequired[DataTrigger | DataTriggerDict]
    notification: NotRequired[Notificationarray | NotificationarrayDict]
