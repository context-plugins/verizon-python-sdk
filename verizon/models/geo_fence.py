from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.type import TypeOrStr
from .feature_item import FeatureItem, FeatureItemDict


class GeoFence(SdkBaseModel):
    """The GeoJSON representation of geofence. Geofence supports the following geometry types: LineString, Polygon,
    MultiLineString, and MultiPolygon. The system only supports a single Feature in the FeatureCollection, so only one
    Line, Polygon, MultiLine or MultiPolygon can be defined within one Geofencing configuration."""

    type_: TypeOrStr = Field(alias="type")
    features: list[FeatureItem]


class GeoFenceDict(TypedDict):
    type_: TypeOrStr
    features: list[FeatureItem | FeatureItemDict]
