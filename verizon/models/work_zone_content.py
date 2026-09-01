from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .unions.text_phrase_or_itis import TextPhraseOrItis, TextPhraseOrItisDict


class WorkZoneContent(SdkBaseModel):
    """DataFrame content variant carrying work zone information."""

    work_zone: list[TextPhraseOrItis] = Field(alias="workZone")
    """List of work zone signs and directions."""


class WorkZoneContentDict(TypedDict):
    work_zone: list[TextPhraseOrItis | TextPhraseOrItisDict]
