from __future__ import annotations

from typing import Any

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel


class ResourceUser(SdkBaseModel):
    accountclientid: Optional[str] = UNSET
    """Not used in this release, future functionality"""

    ackterms: Optional[bool] = UNSET
    """Indicates if terms are agreed to (true) or not"""

    acktermson: Optional[RFC3339DateTime] = UNSET
    billingaccountid: Optional[str] = UNSET
    """The billing account ID. This is the same value as the Account ID"""

    createdon: RFC3339DateTime
    """Timestamp of the record"""

    credentialsid: Optional[str] = UNSET
    """User credentials. The only valid value is an email address"""

    credentialstype: str
    """The type of credential represented by the ID. The only valid value is ``email``"""

    customdata: Optional[dict[str, Any]] = UNSET
    """Name/value pair, where the value is client defined. The purpose is to keep track of current state per device
    action."""

    description: Optional[str] = UNSET
    """a short description"""

    displayname: Optional[str] = UNSET
    """the user name value to display"""

    email: Optional[str] = UNSET
    """Contact email for the group"""

    firstname: Optional[str] = UNSET
    """The first name in the user record"""

    foreignid: str
    """UUID of the ECPD account the user belongs to"""

    id: Optional[str] = UNSET
    """UUID of the user record, assigned at creation"""

    lastname: Optional[str] = UNSET
    """The last name in the user record"""

    lastupdated: RFC3339DateTime
    """Timestamp of the record"""

    mdn: Optional[str] = UNSET
    """The Mobile Directory Number"""

    middlename: Optional[str] = UNSET
    """optional field for middle name or initial"""

    name: Optional[str] = UNSET
    """User defined name of the record"""

    secondarybillingaccountids: Optional[list[str]] = UNSET
    """Virtual field; will not be used in this implementation"""

    state: Optional[str] = UNSET
    """The current status of the device or transaction and will be ``success`` or ``failed``"""

    version: Optional[str] = UNSET
    """The resource version"""

    versionid: str
    """The UUID of the resource version"""


class ResourceUserDict(TypedDict):
    accountclientid: NotRequired[str]
    ackterms: NotRequired[bool]
    acktermson: NotRequired[RFC3339DateTime]
    billingaccountid: NotRequired[str]
    createdon: RFC3339DateTime
    credentialsid: NotRequired[str]
    credentialstype: str
    customdata: NotRequired[dict[str, Any]]
    description: NotRequired[str]
    displayname: NotRequired[str]
    email: NotRequired[str]
    firstname: NotRequired[str]
    foreignid: str
    id: NotRequired[str]
    lastname: NotRequired[str]
    lastupdated: RFC3339DateTime
    mdn: NotRequired[str]
    middlename: NotRequired[str]
    name: NotRequired[str]
    secondarybillingaccountids: NotRequired[list[str]]
    state: NotRequired[str]
    version: NotRequired[str]
    versionid: str
