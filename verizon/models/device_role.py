from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class DeviceRole(SdkBaseModel):
    """The access rule (DeviceRole object) defines the topics the application or device can publish or subscribe to. It
    also defines how many parallel subscriptions one device or application can have and how fast it can publish
    messages."""

    name: str
    """The unique name of the access rule."""

    subscribe_limit: Optional[int] = Field(default=UNSET, alias="subscribeLimit")
    """The maximum number of subscriptions that one application or device can make."""

    publish_rate_limit: Optional[int] = Field(default=UNSET, alias="publishRateLimit")
    """The maximum rate that one application or device can publish messages per seconds."""

    publish: Optional[list[str]] = UNSET
    subscribe: Optional[list[str]] = UNSET


class DeviceRoleDict(TypedDict):
    name: str
    subscribe_limit: NotRequired[int]
    publish_rate_limit: NotRequired[int]
    publish: NotRequired[list[str]]
    subscribe: NotRequired[list[str]]
