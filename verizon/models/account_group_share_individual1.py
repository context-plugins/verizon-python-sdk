from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .account_group_share_filter_criteria import AccountGroupShareFilterCriteria, AccountGroupShareFilterCriteriaDict


class AccountGroupShareIndividual1(SdkBaseModel):
    account_group_share_individual: Optional[AccountGroupShareFilterCriteria] = Field(
        default=UNSET, alias="accountGroupShareIndividual"
    )


class AccountGroupShareIndividual1Dict(TypedDict):
    account_group_share_individual: NotRequired[AccountGroupShareFilterCriteria | AccountGroupShareFilterCriteriaDict]
