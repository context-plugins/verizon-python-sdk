from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Fields2(SdkBaseModel):
    """List of fields affected by the event."""

    temperature: Optional[str] = UNSET


class Fields2Dict(TypedDict):
    temperature: NotRequired[str]
