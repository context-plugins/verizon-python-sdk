from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .account_identifier import AccountIdentifier, AccountIdentifierDict
from .create_target_request_fields import CreateTargetRequestFields, CreateTargetRequestFieldsDict
from .target_authentication import TargetAuthentication, TargetAuthenticationDict


class CreateTargetRequest(SdkBaseModel):
    """Details of the target that you want to create."""

    accountidentifier: Optional[AccountIdentifier] = UNSET
    """The ID of the authenticating billing account, in the format ``{"billingaccountid":"1234567890-12345"}``."""

    billingaccountid: Optional[str] = UNSET
    """The ID of the authenticating billing account."""

    kind: Optional[str] = UNSET
    """Identifies the resource kind. Targets are ts.target."""

    address: Optional[str] = UNSET
    """The endpoint for notifications or data streams. The format depends on the selected ``addressscheme``.<br
    />``streamrest`` requires a ``host:port`` value <br />``streamawsiot`` requres a valid ARN."""

    addressscheme: Optional[str] = UNSET
    """The transport format. Valid values are: <br />streamawsiot - streamed data to an AWS account <br />streamrest -
    streamed REST data to a defined endpoint."""

    fields: Optional[CreateTargetRequestFields] = UNSET
    description: Optional[str] = UNSET
    """Descriptive information about the target."""

    externalid: Optional[str] = UNSET
    """Security identification string created by a POST /targets/actions/newextid request."""

    name: Optional[str] = UNSET
    """Name of the target."""

    region: Optional[str] = UNSET
    """AWS region value."""

    key1: Optional[str] = UNSET
    """OAuth 2.0 bearer token."""

    oauth: Optional[TargetAuthentication] = UNSET
    """OAuth 2 token and refresh token for TS to stream events to Target."""


class CreateTargetRequestDict(TypedDict):
    accountidentifier: NotRequired[AccountIdentifier | AccountIdentifierDict]
    billingaccountid: NotRequired[str]
    kind: NotRequired[str]
    address: NotRequired[str]
    addressscheme: NotRequired[str]
    fields: NotRequired[CreateTargetRequestFields | CreateTargetRequestFieldsDict]
    description: NotRequired[str]
    externalid: NotRequired[str]
    name: NotRequired[str]
    region: NotRequired[str]
    key1: NotRequired[str]
    oauth: NotRequired[TargetAuthentication | TargetAuthenticationDict]
