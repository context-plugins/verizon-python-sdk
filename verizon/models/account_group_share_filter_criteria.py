from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .account_group_share_action import AccountGroupShareAction, AccountGroupShareActionDict
from .account_group_share_condition import AccountGroupShareCondition, AccountGroupShareConditionDict
from .account_group_share_filter import AccountGroupShareFilter, AccountGroupShareFilterDict


class AccountGroupShareFilterCriteria(SdkBaseModel):
    filter_criteria: Optional[AccountGroupShareFilter] = Field(default=UNSET, alias="filterCriteria")
    condition: Optional[AccountGroupShareCondition] = UNSET
    action: Optional[AccountGroupShareAction] = UNSET


class AccountGroupShareFilterCriteriaDict(TypedDict):
    filter_criteria: NotRequired[AccountGroupShareFilter | AccountGroupShareFilterDict]
    condition: NotRequired[AccountGroupShareCondition | AccountGroupShareConditionDict]
    action: NotRequired[AccountGroupShareAction | AccountGroupShareActionDict]
