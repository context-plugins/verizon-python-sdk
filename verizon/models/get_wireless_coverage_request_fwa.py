from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .locations import Locations, LocationsDict
from .network_type_object import NetworkTypeObject, NetworkTypeObjectDict


class GetWirelessCoverageRequestFwa(SdkBaseModel):
    """Get wireless coverage FWA."""

    account_name: str = Field(alias="accountName")
    """Account name."""

    request_type: str = Field(alias="requestType")
    """Type of request made. FWA for address qualification and NW for Nationwide coverage."""

    location_type: str = Field(alias="locationType")
    """Type of location detail."""

    locations: Locations
    network_types_list: list[NetworkTypeObject] = Field(alias="networkTypesList")


class GetWirelessCoverageRequestFwaDict(TypedDict):
    account_name: str
    request_type: str
    location_type: str
    locations: Locations | LocationsDict
    network_types_list: list[NetworkTypeObject | NetworkTypeObjectDict]
