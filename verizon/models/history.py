from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .device import Device, DeviceDict
from .history_attribute_value import HistoryAttributeValue, HistoryAttributeValueDict


class History(SdkBaseModel):
    """History data for a selected device and its attributes at a specific time."""

    account_name: str = Field(alias="accountName")
    """The name of the billing account for which you want retrieve history data. An account name is usually numeric, and
    must include any leading zeros."""

    device: Device
    """Identifies a particular IoT device."""

    attributes: Optional[HistoryAttributeValue] = UNSET
    """Streaming RF parameter for which you want to retrieve history data."""


class HistoryDict(TypedDict):
    account_name: str
    device: Device | DeviceDict
    attributes: NotRequired[HistoryAttributeValue | HistoryAttributeValueDict]
