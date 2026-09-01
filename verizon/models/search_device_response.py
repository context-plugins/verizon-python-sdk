from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .fields2 import Fields2, Fields2Dict


class SearchDeviceResponse(SdkBaseModel):
    """A success response includes an array of all matching events. Each event includes the full event resource
    definition."""

    action: Optional[str] = UNSET
    """The action requested in this event; “change” for device configuration changes."""

    createdon: Optional[str] = UNSET
    """The date and time of the change request."""

    deviceid: Optional[str] = UNSET
    """The device’s ThingSpace UUID."""

    fields: Optional[Fields2] = UNSET
    """List of fields affected by the event."""

    id: Optional[str] = UNSET
    """The unique ID of this ts.event.configuration event."""

    kind: Optional[str] = UNSET
    """The kind of the ThingSpace resource that is being reported; “ts.event.configuration” for device configuration
    changes."""

    lastupdated: Optional[str] = UNSET
    """The date and time that the event was last updated."""

    name: Optional[str] = UNSET
    """The name of the event"""

    state: Optional[str] = UNSET
    """The current status of the request."""

    tagids: Optional[list[str]] = UNSET
    """UUIDs of tag resources that are applied to this device."""

    transactionid: Optional[str] = UNSET
    """transaction id"""

    version: Optional[str] = UNSET
    """The version of the resource."""

    versionid: Optional[str] = UNSET
    """The version of the resource."""


class SearchDeviceResponseDict(TypedDict):
    action: NotRequired[str]
    createdon: NotRequired[str]
    deviceid: NotRequired[str]
    fields: NotRequired[Fields2 | Fields2Dict]
    id: NotRequired[str]
    kind: NotRequired[str]
    lastupdated: NotRequired[str]
    name: NotRequired[str]
    state: NotRequired[str]
    tagids: NotRequired[list[str]]
    transactionid: NotRequired[str]
    version: NotRequired[str]
    versionid: NotRequired[str]
