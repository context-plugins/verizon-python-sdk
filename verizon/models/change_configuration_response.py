from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .fields import Fields, FieldsDict


class ChangeConfigurationResponse(SdkBaseModel):
    """Change Configuration resource definition."""

    action: Optional[str] = UNSET
    """The action requested in this event; “change” for device configuration changes."""

    createdon: Optional[str] = UNSET
    """The date and time of the change request."""

    deviceid: Optional[str] = UNSET
    """The device’s ThingSpace UUID."""

    fields: Optional[Fields] = UNSET
    """List of fields affected by the event."""

    foreignid: Optional[str] = UNSET
    """foreign id"""

    id: Optional[str] = UNSET
    """The unique ID of this ts.event.configuration event."""

    kind: Optional[str] = UNSET
    """The kind of the ThingSpace resource that is being reported"""

    lastupdated: Optional[str] = UNSET
    """The date and time that the event was last updated."""

    name: Optional[str] = UNSET
    """The name of the event; “SetConfigurationReq” for device configuration changes."""

    state: Optional[str] = UNSET
    """The current status of the request. The value will be “pending” until the device wakes up and ThingSpace can send
    the request to the device."""

    transactionid: Optional[str] = UNSET
    """transaction id"""

    version: Optional[str] = UNSET
    """version"""


class ChangeConfigurationResponseDict(TypedDict):
    action: NotRequired[str]
    createdon: NotRequired[str]
    deviceid: NotRequired[str]
    fields: NotRequired[Fields | FieldsDict]
    foreignid: NotRequired[str]
    id: NotRequired[str]
    kind: NotRequired[str]
    lastupdated: NotRequired[str]
    name: NotRequired[str]
    state: NotRequired[str]
    transactionid: NotRequired[str]
    version: NotRequired[str]
