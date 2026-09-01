from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class EtxMapMessageGeofenceGeometry(str, Enum):
    """Type of the GeoJSON geometry, must be 'Polygon'."""

    POLYGON = "Polygon"

    __str__ = str.__str__


EtxMapMessageGeofenceGeometryOrStr: TypeAlias = Annotated[
    EtxMapMessageGeofenceGeometry | str, open_enum_validator(EtxMapMessageGeofenceGeometry)
]
