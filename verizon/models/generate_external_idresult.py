from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class GenerateExternalIdresult(SdkBaseModel):
    """A new external ID."""

    externalid: Optional[str] = UNSET
    """Newly created security string."""


class GenerateExternalIdresultDict(TypedDict):
    externalid: NotRequired[str]
