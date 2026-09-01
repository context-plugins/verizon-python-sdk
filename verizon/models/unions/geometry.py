from __future__ import annotations

from typing import TypeAlias

from ..line_string import LineString, LineStringDict
from ..multi_line_string import MultiLineString, MultiLineStringDict
from ..multi_polygon import MultiPolygon, MultiPolygonDict
from ..polygon import Polygon, PolygonDict

Geometry: TypeAlias = LineString | Polygon | MultiLineString | MultiPolygon

GeometryDict: TypeAlias = LineStringDict | PolygonDict | MultiLineStringDict | MultiPolygonDict
