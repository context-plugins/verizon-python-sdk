from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .event_type import EventType, EventTypeDict


class Situation(SdkBaseModel):
    """This represents the situation container describing the event and the reliability of the detection source."""

    information_quality: int = Field(alias="informationQuality")
    """The quality or reliability level of the information provided by the ITS-S application of the originating
    ITS-S."""

    event_type: EventType = Field(alias="eventType")
    """The type of event including direct and sub cause."""


class SituationDict(TypedDict):
    information_quality: int
    event_type: EventType | EventTypeDict
