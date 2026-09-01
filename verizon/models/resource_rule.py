from __future__ import annotations

from typing import Any

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel


class ResourceRule(SdkBaseModel):
    accountclientid: Optional[str] = UNSET
    """Not used in this release, future functionality"""

    billingaccountid: Optional[str] = UNSET
    """The billing account ID. This is the same value as the Account ID"""

    createdon: RFC3339DateTime
    """Timestamp of the record"""

    description: Optional[str] = UNSET
    """a short description"""

    deviceid: Optional[str] = UNSET
    """This is a UUID value of the device created when the device is onboarded"""

    disabled: Optional[bool] = UNSET
    foreignid: str
    """UUID of the ECPD account the user belongs to"""

    id: Optional[str] = UNSET
    """UUID of the user record, assigned at creation"""

    lastupdated: RFC3339DateTime
    """Timestamp of the record"""

    name: Optional[str] = UNSET
    """User defined name of the record"""

    rulechain: Any
    rulesyntax: Optional[str] = UNSET
    """The syntax of the rule and supports camel and json style syntaxes"""

    version: Optional[str] = UNSET
    """The resource version"""

    versionid: str
    """The UUID of the resource version"""


class ResourceRuleDict(TypedDict):
    accountclientid: NotRequired[str]
    billingaccountid: NotRequired[str]
    createdon: RFC3339DateTime
    description: NotRequired[str]
    deviceid: NotRequired[str]
    disabled: NotRequired[bool]
    foreignid: str
    id: NotRequired[str]
    lastupdated: RFC3339DateTime
    name: NotRequired[str]
    rulechain: Any
    rulesyntax: NotRequired[str]
    version: NotRequired[str]
    versionid: str
