from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Subscription(SdkBaseModel):
    """Subscription resource definition."""

    configurationfailures: Optional[int] = UNSET
    """The number of streaming failures due to faulty configuration."""

    createdon: Optional[str] = UNSET
    """The number of streaming failures due to faulty configuration."""

    delegateid: Optional[str] = UNSET
    """Not currently used."""

    description: Optional[str] = UNSET
    """Description of the subscription."""

    disabled: Optional[bool] = UNSET
    """Whether the subscription is currently sending data."""

    email: Optional[str] = UNSET
    """The address to which any error reports should be delivered."""

    filter: Optional[str] = UNSET
    """Filter for events."""

    id: Optional[str] = UNSET
    """ThingSpace unique ID for the subscription that was created."""

    kind: Optional[str] = UNSET
    """Identifies the resource kind."""

    laststreamingstatus: Optional[str] = UNSET
    """Possible values: success or fail."""

    laststreamingtime: Optional[str] = UNSET
    """The date and time that the last stream send was attempted."""

    lastupdated: Optional[str] = UNSET
    """The date the resource was last updated."""

    name: Optional[str] = UNSET
    """Name of the subscription."""

    networkfailures: Optional[int] = UNSET
    """The number of failures due to network problems."""

    streamfailures: Optional[int] = UNSET
    streamkind: Optional[str] = UNSET
    """The event type that will be sent in the data stream."""

    targetid: Optional[str] = UNSET
    """Target to be used for dispatching events."""

    targettype: Optional[str] = UNSET
    version: Optional[str] = UNSET
    """Version of the underlying schema resource."""

    versionid: Optional[str] = UNSET
    """The version of the resource."""


class SubscriptionDict(TypedDict):
    configurationfailures: NotRequired[int]
    createdon: NotRequired[str]
    delegateid: NotRequired[str]
    description: NotRequired[str]
    disabled: NotRequired[bool]
    email: NotRequired[str]
    filter: NotRequired[str]
    id: NotRequired[str]
    kind: NotRequired[str]
    laststreamingstatus: NotRequired[str]
    laststreamingtime: NotRequired[str]
    lastupdated: NotRequired[str]
    name: NotRequired[str]
    networkfailures: NotRequired[int]
    streamfailures: NotRequired[int]
    streamkind: NotRequired[str]
    targetid: NotRequired[str]
    targettype: NotRequired[str]
    version: NotRequired[str]
    versionid: NotRequired[str]
