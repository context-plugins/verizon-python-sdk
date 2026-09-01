from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Accountid(SdkBaseModel):
    account_name: Optional[str] = Field(default=UNSET, alias="accountName")
    """The numeric name of the account and must include leading zeroes"""

    mtas_account_number: Optional[str] = Field(default=UNSET, alias="mtasAccountNumber")


class AccountidDict(TypedDict):
    account_name: NotRequired[str]
    mtas_account_number: NotRequired[str]
