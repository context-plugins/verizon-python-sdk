from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .coordinates import Coordinates, CoordinatesDict


class GetNetworkConditionsRequest(SdkBaseModel):
    """Get network conditions."""

    account_name: str = Field(alias="accountName")
    """Account name."""

    location_type: str = Field(alias="locationType")
    """Type of location detail."""

    coordinates: Coordinates
    """Coordinates information."""


class GetNetworkConditionsRequestDict(TypedDict):
    account_name: str
    location_type: str
    coordinates: Coordinates | CoordinatesDict
