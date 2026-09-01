from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class ActionId(SdkBaseModel):
    originating_station_id: int = Field(alias="originatingStationId")
    """Unique ID for originating station."""

    sequence_number: int = Field(alias="sequenceNumber")
    """Counter used to differenciate multiple DENMs from same station."""


class ActionIdDict(TypedDict):
    originating_station_id: int
    sequence_number: int
