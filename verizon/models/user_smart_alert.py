from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel


class UserSmartAlert(SdkBaseModel):
    accountclientid: Optional[str] = UNSET
    """Not used in this release, future functionality"""

    billingaccountid: Optional[str] = UNSET
    """The billing account ID. This is the same value as the Account ID"""

    category: Optional[str] = UNSET
    """The type of alert and will be either ``telemetry`` or ``infrastructure``"""

    condition: Optional[int] = UNSET
    """The condition or threshold for an alert"""

    createdon: RFC3339DateTime
    """Timestamp of the record"""

    description: Optional[str] = UNSET
    """a short description"""

    deviceid: Optional[str] = UNSET
    """This is a UUID value of the device created when the device is onboarded"""

    foreignid: Optional[str] = UNSET
    """UUID of the ECPD account the user belongs to"""

    id: Optional[str] = UNSET
    """UUID of the user record, assigned at creation"""

    isacknowledged: Optional[bool] = UNSET
    """A flag that indicates if the alarm has been acknowledged"""

    iscleared: Optional[bool] = UNSET
    """A flag that indicates if the alarm has been cleared"""

    isdisabled: Optional[bool] = UNSET
    """A flag that indicates if the alarm has been disabled"""

    lastupdated: RFC3339DateTime
    """Timestamp of the record"""

    name: Optional[str] = UNSET
    """User defined name of the record"""

    ruleid: Optional[str] = UNSET
    """The UUID of a rule for alerts"""

    severity: Optional[str] = UNSET
    """The threshold value to trigger an alert and will be Critical, Major or Minor"""

    state: Optional[str] = UNSET
    """The current status of the device or transaction and will be ``success`` or ``failed``"""

    template: Optional[str] = UNSET
    """template of the rule which triggered a given alert"""

    version: Optional[str] = UNSET
    """The resource version"""

    versionid: str
    """The UUID of the resource version"""


class UserSmartAlertDict(TypedDict):
    accountclientid: NotRequired[str]
    billingaccountid: NotRequired[str]
    category: NotRequired[str]
    condition: NotRequired[int]
    createdon: RFC3339DateTime
    description: NotRequired[str]
    deviceid: NotRequired[str]
    foreignid: NotRequired[str]
    id: NotRequired[str]
    isacknowledged: NotRequired[bool]
    iscleared: NotRequired[bool]
    isdisabled: NotRequired[bool]
    lastupdated: RFC3339DateTime
    name: NotRequired[str]
    ruleid: NotRequired[str]
    severity: NotRequired[str]
    state: NotRequired[str]
    template: NotRequired[str]
    version: NotRequired[str]
    versionid: str
