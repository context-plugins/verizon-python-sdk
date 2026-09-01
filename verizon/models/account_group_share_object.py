from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .account_group_share_individual1 import AccountGroupShareIndividual1, AccountGroupShareIndividual1Dict


class AccountGroupShareObject(SdkBaseModel):
    account_group_share: Optional[AccountGroupShareIndividual1] = Field(default=UNSET, alias="accountGroupShare")


class AccountGroupShareObjectDict(TypedDict):
    account_group_share: NotRequired[AccountGroupShareIndividual1 | AccountGroupShareIndividual1Dict]
