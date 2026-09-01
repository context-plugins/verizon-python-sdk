from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .account_identifier import AccountIdentifier, AccountIdentifierDict
from .resource_identifier import ResourceIdentifier, ResourceIdentifierDict


class RemoveDeviceRequest(SdkBaseModel):
    """The request body identifies the device to delete."""

    accountidentifier: AccountIdentifier
    """The ID of the authenticating billing account, in the format ``{"billingaccountid":"1234567890-12345"}``."""

    resourceidentifier: ResourceIdentifier
    """The ID of the target to delete, in the format {"id": "dd1682d3-2d80-cefc-f3ee-25154800beff"}."""


class RemoveDeviceRequestDict(TypedDict):
    accountidentifier: AccountIdentifier | AccountIdentifierDict
    resourceidentifier: ResourceIdentifier | ResourceIdentifierDict
