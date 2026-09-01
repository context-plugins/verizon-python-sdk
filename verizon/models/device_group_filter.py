from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class DeviceGroupFilter(SdkBaseModel):
    device_group_name: Optional[str] = Field(default=UNSET, alias="deviceGroupName")
    individual_or_combined: Optional[str] = Field(default=UNSET, alias="IndividualOrCombined")
    account_name: Optional[str] = Field(default=UNSET, alias="accountName")
    """The numeric name of the account and must include leading zeroes"""


class DeviceGroupFilterDict(TypedDict):
    device_group_name: NotRequired[str]
    individual_or_combined: NotRequired[str]
    account_name: NotRequired[str]
