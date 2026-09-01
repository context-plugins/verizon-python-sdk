from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.etx_map_message_geofence_geometry import EtxMapMessageGeofenceGeometryOrStr


class GeofencePolygon(SdkBaseModel):
    """GeoJSON Polygon geofence object."""

    type_: Optional[EtxMapMessageGeofenceGeometryOrStr] = Field(default=UNSET, alias="type")
    """Type of the GeoJSON geometry, must be 'Polygon'."""

    coordinates: Optional[list[list[float]]] = UNSET
    """Coordinates of the GeoJSON polygon. Rules for a valid GeoJSON Polygon:
    - Must contain between 4 and 50 points.
    - Must be an array of linear rings (arrays of positions).
    - The first linear ring represents the outer boundary; subsequent rings would represent holes. Holes are not
        supported, so only one linear ring should be defined in a polygon.
    - Each linear ring must have at least 4 positions, and the first and last positions must be identical to close the
        polygon ring.
    - A linear ring must follow the right-hand rule with respect to the area it bounds: exterior rings (outer boundery)
        are counterclockwise.
    - Each position is an array of two numbers: [longitude, latitude].
    - Longitude and latitude values must be in decimal degrees.
    - Longitude must be ranging from -180 to 180.
    - Latitude must be ranging from -90 to 90.
    - The polygon must not self-intersect."""


class GeofencePolygonDict(TypedDict):
    type_: NotRequired[EtxMapMessageGeofenceGeometryOrStr]
    coordinates: NotRequired[list[list[float]]]
