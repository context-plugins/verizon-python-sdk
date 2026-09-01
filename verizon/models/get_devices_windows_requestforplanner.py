from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .device_listforplanner import DeviceListforplanner, DeviceListforplannerDict


class GetDevicesWindowsRequestforplanner(SdkBaseModel):
    account_number: OptionalNullable[str] = Field(default=UNSET, alias="accountNumber")
    """The numeric name of the account, including leading zeros."""

    filter: OptionalNullable[str] = UNSET
    """what windows to filter for: All - all 24 windows in a day, Best - top 3 windows by RAN KPI, Worst - lowest 3
    windows by RAN KPI"""

    devices: Optional[list[DeviceListforplanner | None]] = UNSET


class GetDevicesWindowsRequestforplannerDict(TypedDict):
    account_number: NotRequired[str | None]
    filter: NotRequired[str | None]
    devices: NotRequired[list[DeviceListforplanner | DeviceListforplannerDict | None]]
