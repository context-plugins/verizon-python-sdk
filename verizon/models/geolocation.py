from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Geolocation(SdkBaseModel):
    """Geolocation of the device at the time of the connection request in GPS coordinates."""

    latitude: float = Field(alias="Latitude")
    """The GPS Latitude value"""

    longitude: float = Field(alias="Longitude")
    """The GPS Longitude value"""


class GeolocationDict(TypedDict):
    latitude: float
    longitude: float
