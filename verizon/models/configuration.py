from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Configuration(SdkBaseModel):
    """List of the field names and values to set."""

    frequency: Optional[str] = UNSET


class ConfigurationDict(TypedDict):
    frequency: NotRequired[str]
