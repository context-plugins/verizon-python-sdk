from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .account_share_filter_criteria1 import AccountShareFilterCriteria1, AccountShareFilterCriteria1Dict


class AccountShareFilterCriteria(SdkBaseModel):
    filter_criteria: Optional[AccountShareFilterCriteria1] = Field(default=UNSET, alias="filterCriteria")


class AccountShareFilterCriteriaDict(TypedDict):
    filter_criteria: NotRequired[AccountShareFilterCriteria1 | AccountShareFilterCriteria1Dict]
