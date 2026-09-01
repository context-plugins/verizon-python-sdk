from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class HyperPreciseLocationFault(SdkBaseModel):
    """Fault occurred while responding."""

    code: Optional[str] = UNSET
    """Hyper precise location fault code."""

    message: Optional[str] = UNSET
    """Hyper precise location fault message."""

    description: Optional[str] = UNSET
    """Hyper precise location fault description."""


class HyperPreciseLocationFaultDict(TypedDict):
    code: NotRequired[str]
    message: NotRequired[str]
    description: NotRequired[str]
