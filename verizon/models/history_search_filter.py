from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .device import Device, DeviceDict
from .history_search_filter_attributes import HistorySearchFilterAttributes, HistorySearchFilterAttributesDict


class HistorySearchFilter(SdkBaseModel):
    """The selected device and attributes for which a request should retrieve data."""

    account_name: str = Field(alias="accountName")
    """Account name identifier."""

    device: Device
    """Identifies a particular IoT device."""

    attributes: Optional[HistorySearchFilterAttributes] = UNSET
    """Streaming RF parameters for which you want to retrieve history data."""


class HistorySearchFilterDict(TypedDict):
    account_name: str
    device: Device | DeviceDict
    attributes: NotRequired[HistorySearchFilterAttributes | HistorySearchFilterAttributesDict]
