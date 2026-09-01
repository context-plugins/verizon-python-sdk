from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .device_id import DeviceId, DeviceIdDict


class NotificationReportStatusRequest(SdkBaseModel):
    account_name: str = Field(alias="accountName")
    """The name of a billing account."""

    device: DeviceId
    """An identifier for a single device."""

    request_type: str = Field(alias="requestType")
    """The type of request."""

    request_expiration_time: Optional[str] = Field(default=UNSET, alias="requestExpirationTime")
    """The time at which the request expires."""


class NotificationReportStatusRequestDict(TypedDict):
    account_name: str
    device: DeviceId | DeviceIdDict
    request_type: str
    request_expiration_time: NotRequired[str]
