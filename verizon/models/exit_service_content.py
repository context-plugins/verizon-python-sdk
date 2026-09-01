from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .unions.text_phrase_or_itis import TextPhraseOrItis, TextPhraseOrItisDict


class ExitServiceContent(SdkBaseModel):
    """DataFrame content variant carrying exit service information."""

    exit_service: list[TextPhraseOrItis] = Field(alias="exitService")
    """List of roadside available services."""


class ExitServiceContentDict(TypedDict):
    exit_service: list[TextPhraseOrItis | TextPhraseOrItisDict]
