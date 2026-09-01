from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .v3_device_list_item import V3DeviceListItem, V3DeviceListItemDict


class V3AddOrRemoveDeviceResult(SdkBaseModel):
    """Add or remove devices to existing upgrade information."""

    account_name: str = Field(alias="accountName")
    """Account identifier."""

    campaign_id: str = Field(alias="campaignId")
    """Campaign identifier."""

    device_list: list[V3DeviceListItem] = Field(alias="deviceList")
    """Array of devices changed."""


class V3AddOrRemoveDeviceResultDict(TypedDict):
    account_name: str
    campaign_id: str
    device_list: list[V3DeviceListItem | V3DeviceListItemDict]
