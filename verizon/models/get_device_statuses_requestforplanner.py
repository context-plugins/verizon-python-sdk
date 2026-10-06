from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel
from .device_listforplanner import DeviceListforplanner, DeviceListforplannerDict


class GetDeviceStatusesRequestforplanner(SdkBaseModel):
    account_number: OptionalNullable[str] = Field(default=UNSET, alias="accountNumber")
    """The numeric name of the account, including leading zeros."""

    request_id: OptionalNullable[str] = Field(default=UNSET, alias="requestId")
    """The unique ID of a request. This is a UUID value."""

    devices: OptionalNullable[list[DeviceListforplanner]] = UNSET


class GetDeviceStatusesRequestforplannerDict(TypedDict):
    account_number: NotRequired[str | None]
    request_id: NotRequired[str | None]
    devices: NotRequired[list[DeviceListforplannerDict] | None]
