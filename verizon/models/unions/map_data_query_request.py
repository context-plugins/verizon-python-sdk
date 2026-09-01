from __future__ import annotations

from typing import TypeAlias

from ..etx_map_message_geo_json_polygon import EtxMapMessageGeoJsonPolygon, EtxMapMessageGeoJsonPolygonDict
from ..etx_map_message_intersection_coordinates import (
    EtxMapMessageIntersectionCoordinates,
    EtxMapMessageIntersectionCoordinatesDict,
)

MapDataQueryRequest: TypeAlias = EtxMapMessageIntersectionCoordinates | EtxMapMessageGeoJsonPolygon
"""Request structure for querying MAP records. Provide either regionIntersectionPairs (coordinates) or geoJson, not
both."""

MapDataQueryRequestDict: TypeAlias = EtxMapMessageIntersectionCoordinatesDict | EtxMapMessageGeoJsonPolygonDict
