from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ConfigurationListItem(SdkBaseModel):
    """The ConfigurationList's item that contains the configuration identifier, name, description and the active
    flag."""

    id: str
    """The generated ID (UUID v4) for the configuration. It has to be used when asking for changing any of the
    configuration parameters."""

    name: Optional[str] = UNSET
    """Name of the configuration."""

    description: Optional[str] = UNSET
    """Description of the configuration."""

    is_active: bool = Field(alias="isActive")


class ConfigurationListItemDict(TypedDict):
    id: str
    name: NotRequired[str]
    description: NotRequired[str]
    is_active: bool
