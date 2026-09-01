from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel


class UserDeviceExperienceHistory(SdkBaseModel):
    billingaccountid: Optional[str] = UNSET
    """The billing account ID. This is the same value as the Account ID"""

    createdon: Optional[RFC3339DateTime] = UNSET
    """Timestamp of the record"""

    date: Optional[RFC3339DateTime] = UNSET
    """Timestamp of the record"""

    devicesbad: Optional[int] = UNSET
    """This is a score based on combination of network coverage and network outage affecting the device's ability to
    connect to the network. This is a count of devices that have failed"""

    devicesfair: Optional[int] = UNSET
    """This is a score based on combination of network coverage and network outage affecting the device's ability to
    connect to the network. This is a count of devices that are impaired"""

    devicesgood: Optional[int] = UNSET
    """This is a score based on combination of network coverage and network outage affecting the device's ability to
    connect to the network. This is a count of devices that have no issues"""

    devicestotal: Optional[int] = UNSET
    """A count of all devices"""

    foreignid: Optional[str] = UNSET
    """UUID of the ECPD account the user belongs to"""

    id: Optional[str] = UNSET
    """UUID of the user record, assigned at creation"""

    lastupdated: Optional[RFC3339DateTime] = UNSET
    """Timestamp of the record"""

    version: Optional[str] = UNSET
    """The resource version"""

    versionid: Optional[str] = UNSET
    """The UUID of the resource version"""


class UserDeviceExperienceHistoryDict(TypedDict):
    billingaccountid: NotRequired[str]
    createdon: NotRequired[RFC3339DateTime]
    date: NotRequired[RFC3339DateTime]
    devicesbad: NotRequired[int]
    devicesfair: NotRequired[int]
    devicesgood: NotRequired[int]
    devicestotal: NotRequired[int]
    foreignid: NotRequired[str]
    id: NotRequired[str]
    lastupdated: NotRequired[RFC3339DateTime]
    version: NotRequired[str]
    versionid: NotRequired[str]
