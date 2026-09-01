from __future__ import annotations

from typing import Any

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class AccountConsentCreate(SdkBaseModel):
    device_list: Optional[list[Any]] = Field(default=UNSET, alias="deviceList")
    """An array of device identifiers"""

    account_name: Optional[str] = Field(default=UNSET, alias="accountName")
    """The numeric name of the account, including leading zeros."""


class AccountConsentCreateDict(TypedDict):
    device_list: NotRequired[list[Any]]
    account_name: NotRequired[str]
