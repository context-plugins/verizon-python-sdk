from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .custom_fields import CustomFields, CustomFieldsDict


class ConnectionEvent(SdkBaseModel):
    """Network connection events for a device during a specified time period."""

    connection_event_attributes: Optional[list[CustomFields]] = Field(default=UNSET, alias="connectionEventAttributes")
    """The attributes that describe the connection event."""

    extended_attributes: Optional[list[CustomFields]] = Field(default=UNSET, alias="extendedAttributes")
    """Currently not used."""

    occurred_at: Optional[str] = Field(default=UNSET, alias="occurredAt")
    """The date and time when the connection event occured."""


class ConnectionEventDict(TypedDict):
    connection_event_attributes: NotRequired[list[CustomFields | CustomFieldsDict]]
    extended_attributes: NotRequired[list[CustomFields | CustomFieldsDict]]
    occurred_at: NotRequired[str]
