from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .account_identifier import AccountIdentifier, AccountIdentifierDict


class CreateSubscriptionRequest(SdkBaseModel):
    """The details of the subscription that you want to create."""

    accountidentifier: Optional[AccountIdentifier] = UNSET
    """The ID of the authenticating billing account, in the format ``{"billingaccountid":"1234567890-12345"}``."""

    description: Optional[str] = UNSET
    """Descriptive information about the subscription."""

    disabled: Optional[bool] = UNSET
    """Enable or disable the subscription. A disabled subscription will not send any data."""

    email: Optional[str] = UNSET
    """The address to which any error reports should be delivered."""

    filter: Optional[str] = UNSET
    """String containing a $filter object with a property and value to filter out non-matching events."""

    billingaccountid: Optional[str] = UNSET
    streamkind: Optional[str] = UNSET
    """The type of event data to send via this subscription. This will be ``ts.event`` in most cases. Other event types
    are ``ts.event.diagnostics`` for device diagnostic data, ``ts.event.configuration`` for device configuration events,
    or ``ts.event.security``. Note that the device ThingSpace client must support sending specific event types for
    anything other than ``ts.event``."""

    targetid: Optional[str] = UNSET
    """The ID of the target resource to be used when dispatching events. The corresponding target should have a “stream”
    addressscheme."""

    name: Optional[str] = UNSET
    """Name of the subscription."""

    allowaggregation: Optional[bool] = UNSET
    """Setting this value to ``false`` prevents the data returned from being aggregated and makes the data easier to
    parse."""


class CreateSubscriptionRequestDict(TypedDict):
    accountidentifier: NotRequired[AccountIdentifier | AccountIdentifierDict]
    description: NotRequired[str]
    disabled: NotRequired[bool]
    email: NotRequired[str]
    filter: NotRequired[str]
    billingaccountid: NotRequired[str]
    streamkind: NotRequired[str]
    targetid: NotRequired[str]
    name: NotRequired[str]
    allowaggregation: NotRequired[bool]
