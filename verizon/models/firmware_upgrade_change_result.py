from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .v1_device_list_item import V1DeviceListItem, V1DeviceListItemDict


class FirmwareUpgradeChangeResult(SdkBaseModel):
    """Upgrade information."""

    account_name: Optional[str] = Field(default=UNSET, alias="accountName")
    """Account identifier in "##########-#####"."""

    id: Optional[str] = UNSET
    """The unique identifier for this upgrade."""

    device_list: Optional[list[V1DeviceListItem]] = Field(default=UNSET, alias="deviceList")
    """A JSON object for each device that was included in the request, showing the device IMEI, the status of the
    addition or removal, and additional information about the status."""


class FirmwareUpgradeChangeResultDict(TypedDict):
    account_name: NotRequired[str]
    id: NotRequired[str]
    device_list: NotRequired[list[V1DeviceListItem | V1DeviceListItemDict]]
