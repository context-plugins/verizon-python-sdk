from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .account_level_object import AccountLevelObject, AccountLevelObjectDict


class DataTrigger(SdkBaseModel):
    account_level: Optional[AccountLevelObject] = Field(default=UNSET, alias="accountLevel")


class DataTriggerDict(TypedDict):
    account_level: NotRequired[AccountLevelObject | AccountLevelObjectDict]
