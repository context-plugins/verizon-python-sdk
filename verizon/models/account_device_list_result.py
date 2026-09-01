from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .thingspace_device import ThingspaceDevice, ThingspaceDeviceDict


class AccountDeviceListResult(SdkBaseModel):
    """Response for a request to list down account devices."""

    devices: Optional[list[ThingspaceDevice]] = UNSET
    """Up to 10,000 devices that you want to move to a different account, specified by device identifier."""

    has_more_data: Optional[bool] = Field(default=UNSET, alias="hasMoreData")
    """False for a status 200 response.True for a status 202 response, indicating that there is more data to be
    retrieved."""


class AccountDeviceListResultDict(TypedDict):
    devices: NotRequired[list[ThingspaceDevice | ThingspaceDeviceDict]]
    has_more_data: NotRequired[bool]
