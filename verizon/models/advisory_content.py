from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .unions.advisory_item import AdvisoryItem, AdvisoryItemDict


class AdvisoryContent(SdkBaseModel):
    """DataFrame content variant carrying advisory ITIS codes."""

    advisory: list[AdvisoryItem]
    """List of typical ITIS warnings."""


class AdvisoryContentDict(TypedDict):
    advisory: list[AdvisoryItem | AdvisoryItemDict]
