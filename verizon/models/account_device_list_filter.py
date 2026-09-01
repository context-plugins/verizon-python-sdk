from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .device_id_search import DeviceIdSearch, DeviceIdSearchDict


class AccountDeviceListFilter(SdkBaseModel):
    """Filter for a list of devices."""

    device_identifier_filters: list[DeviceIdSearch] = Field(alias="deviceIdentifierFilters")
    """Specify the kind of the device identifier, the type of match, and the string that you want to match."""


class AccountDeviceListFilterDict(TypedDict):
    device_identifier_filters: list[DeviceIdSearch | DeviceIdSearchDict]
