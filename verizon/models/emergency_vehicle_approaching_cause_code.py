from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class EmergencyVehicleApproachingCauseCode(SdkBaseModel):
    """Cause code wrapper for emergency vehicle approaching events."""

    emergency_vehicle_approaching95: int = Field(alias="emergencyVehicleApproaching95")
    """The value shall be set to:
    - 0 ``unavailable`` - in case further detailed information on the emergency vehicle approaching event is
        unavailable,
    - 1 ``emergencyVehicleApproaching`` - in case an operating emergency vehicle is approaching,
    - 2 ``prioritizedVehicleApproaching`` - in case a prioritized vehicle is approaching,
    - 3-255 - reserved for future usage."""


class EmergencyVehicleApproachingCauseCodeDict(TypedDict):
    emergency_vehicle_approaching95: int
