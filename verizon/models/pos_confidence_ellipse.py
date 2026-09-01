from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class PosConfidenceEllipse(SdkBaseModel):
    semi_major_confidence: int = Field(alias="semiMajorConfidence")
    """Absolute position accuracy in one of the axis direction as defined in a shape of ellipse with a predefined
    confidence level (set to 4095 when unavailable). The value shall be set to:
    - ``n`` (``n > 0`` and ``n < 4094``) if the accuracy is equal to or less than n * 0,01 metre,
    - ``4094`` if the accuracy is out of range, i.e. greater than 4,093 m,
    - ``4095`` if the accuracy information is unavailable.
    The value 0 shall not be used."""

    semi_minor_confidence: int = Field(alias="semiMinorConfidence")
    """Absolute position accuracy in one of the axis direction as defined in a shape of ellipse with a predefined
    confidence level (set to 4095 when unavailable). The value shall be set to:
    - ``n`` (``n > 0`` and ``n < 4094``) if the accuracy is equal to or less than n * 0,01 metre,
    - ``4094`` if the accuracy is out of range, i.e. greater than 4,093 m,
    - ``4095`` if the accuracy information is unavailable.
    The value 0 shall not be used."""

    semi_major_orientation: int = Field(alias="semiMajorOrientation")
    """An angle value in degrees described in the WGS84 reference system with respect to the WGS84 north. The value
    shall be set to:
    - wgs84North (0),
    - wgs84East (900),
    - wgs84South (1800),
    - wgs84West (2700),
    - doNotUse (3600),
    - unavailable (3601)"""


class PosConfidenceEllipseDict(TypedDict):
    semi_major_confidence: int
    semi_minor_confidence: int
    semi_major_orientation: int
