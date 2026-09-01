from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .locationscoord import Locationscoord, LocationscoordDict
from .network_type_object import NetworkTypeObject, NetworkTypeObjectDict


class GetWirelessCoverageRequest(SdkBaseModel):
    """Get wireless coverage."""

    account_name: str = Field(alias="accountName")
    """Account name."""

    request_type: str = Field(alias="requestType")
    """Type of request made. FWA for address qualification and NW for Nationwide coverage."""

    location_type: str = Field(alias="locationType")
    """Type of location detail."""

    locations: Locationscoord
    network_types_list: list[NetworkTypeObject] = Field(alias="networkTypesList")


class GetWirelessCoverageRequestDict(TypedDict):
    account_name: str
    request_type: str
    location_type: str
    locations: Locationscoord | LocationscoordDict
    network_types_list: list[NetworkTypeObject | NetworkTypeObjectDict]
