from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .accountnames import Accountnames, AccountnamesDict


class AccountLevelFilter(SdkBaseModel):
    separate_or_combined: Optional[str] = Field(default=UNSET, alias="separateOrCombined")
    """Determines whether or not to aggregate usage of multiple accounts together, or separate by account. If this is
    null or not present, then the trigger will be for an individual line."""

    account_names: Optional[Accountnames] = Field(default=UNSET, alias="accountNames")


class AccountLevelFilterDict(TypedDict):
    separate_or_combined: NotRequired[str]
    account_names: NotRequired[Accountnames | AccountnamesDict]
