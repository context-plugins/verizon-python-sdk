from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .device_status_itemforplanner import DeviceStatusItemforplanner, DeviceStatusItemforplannerDict


class GetDeviceStatusesResponseforplanner(SdkBaseModel):
    account_number: OptionalNullable[str] = Field(default=UNSET, alias="accountNumber")
    """The numeric name of the account, including leading zeros."""

    request_id: OptionalNullable[str] = Field(default=UNSET, alias="requestId")
    device_status_list: Optional[list[DeviceStatusItemforplanner | None]] = Field(
        default=UNSET, alias="deviceStatusList"
    )


class GetDeviceStatusesResponseforplannerDict(TypedDict):
    account_number: NotRequired[str | None]
    request_id: NotRequired[str | None]
    device_status_list: NotRequired[list[DeviceStatusItemforplanner | DeviceStatusItemforplannerDict | None]]
