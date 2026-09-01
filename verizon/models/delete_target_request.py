from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .account_identifier import AccountIdentifier, AccountIdentifierDict
from .resource_identifier import ResourceIdentifier, ResourceIdentifierDict


class DeleteTargetRequest(SdkBaseModel):
    """Target to delete."""

    accountidentifier: Optional[AccountIdentifier] = UNSET
    """The ID of the authenticating billing account, in the format ``{"billingaccountid":"1234567890-12345"}``."""

    resourceidentifier: Optional[ResourceIdentifier] = UNSET
    """The ID of the target to delete, in the format {"id": "dd1682d3-2d80-cefc-f3ee-25154800beff"}."""


class DeleteTargetRequestDict(TypedDict):
    accountidentifier: NotRequired[AccountIdentifier | AccountIdentifierDict]
    resourceidentifier: NotRequired[ResourceIdentifier | ResourceIdentifierDict]
