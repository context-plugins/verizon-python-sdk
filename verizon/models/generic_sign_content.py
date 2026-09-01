from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .unions.text_phrase_or_itis import TextPhraseOrItis, TextPhraseOrItisDict


class GenericSignContent(SdkBaseModel):
    """DataFrame content variant carrying generic sign information."""

    generic_sign: list[TextPhraseOrItis] = Field(alias="genericSign")
    """List of MUTCD signs and directions."""


class GenericSignContentDict(TypedDict):
    generic_sign: list[TextPhraseOrItis | TextPhraseOrItisDict]
