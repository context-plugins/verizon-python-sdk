from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .configuration import Configuration, ConfigurationDict


class Fields(SdkBaseModel):
    """List of fields affected by the event."""

    configuration: Optional[Configuration] = UNSET
    """List of the field names and values to set."""


class FieldsDict(TypedDict):
    configuration: NotRequired[Configuration | ConfigurationDict]
