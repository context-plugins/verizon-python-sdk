from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class AccountGroupShareFilter(SdkBaseModel):
    rate_plan_group_id: Optional[int] = Field(default=UNSET, alias="ratePlanGroupId")


class AccountGroupShareFilterDict(TypedDict):
    rate_plan_group_id: NotRequired[int]
