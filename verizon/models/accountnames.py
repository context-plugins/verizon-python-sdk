from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Accountnames(SdkBaseModel):
    account_name_list: Optional[list[str]] = Field(default=UNSET, alias="accountNameList")


class AccountnamesDict(TypedDict):
    account_name_list: NotRequired[list[str]]
