from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .unions.text_phrase_or_itis import TextPhraseOrItis, TextPhraseOrItisDict


class SpeedLimitContent(SdkBaseModel):
    """DataFrame content variant carrying speed limit information."""

    speed_limit: list[TextPhraseOrItis] = Field(alias="speedLimit")
    """List of speed limits and cautions."""


class SpeedLimitContentDict(TypedDict):
    speed_limit: list[TextPhraseOrItis | TextPhraseOrItisDict]
