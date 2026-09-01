from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .account_level_filter import AccountLevelFilter, AccountLevelFilterDict
from .enums.account_level_action import AccountLevelActionOrStr
from .unions.account_level_objectcondition import AccountLevelObjectcondition, AccountLevelObjectconditionDict


class AccountLevelObject(SdkBaseModel):
    filter_criteria: Optional[AccountLevelFilter] = Field(default=UNSET, alias="filterCriteria")
    condition: Optional[AccountLevelObjectcondition] = UNSET
    action: Optional[AccountLevelActionOrStr] = UNSET
    """The action taken when trigger conditions are met"""


class AccountLevelObjectDict(TypedDict):
    filter_criteria: NotRequired[AccountLevelFilter | AccountLevelFilterDict]
    condition: NotRequired[AccountLevelObjectcondition | AccountLevelObjectconditionDict]
    action: NotRequired[AccountLevelActionOrStr]
