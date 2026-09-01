from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel
from .dto_fields import DtoFields, DtoFieldsDict


class ResourceEvent(SdkBaseModel):
    accountclientid: Optional[str] = UNSET
    """Not used in this release, future functionality"""

    callbackurl: Optional[str] = UNSET
    """The URL of the callback listener"""

    createdon: RFC3339DateTime
    """Timestamp of the record"""

    description: Optional[str] = UNSET
    """a short description"""

    deviceid: Optional[str] = UNSET
    """This is a UUID value of the device created when the device is onboarded"""

    errmsg: Optional[str] = UNSET
    """Error message"""

    fieldid: str
    fields: Optional[DtoFields] = UNSET
    """Fields to return needed by search"""

    fieldvalue: Optional[list[int]] = UNSET
    foreignid: str
    """UUID of the ECPD account the user belongs to"""

    id: Optional[str] = UNSET
    """UUID of the user record, assigned at creation"""

    lastupdated: RFC3339DateTime
    """Timestamp of the record"""

    modelid: Optional[str] = UNSET
    """The model ID of the device"""

    name: Optional[str] = UNSET
    """User defined name of the record"""

    sensordataaggregation: Optional[bool] = UNSET
    """A flag to indicate if sensor data is to be aggregated (true) or not"""

    state: str
    """The current status of the device or transaction and will be ``success`` or ``failed``"""

    transactionid: Optional[str] = UNSET
    """The system-generated UUID of the transaction"""

    version: Optional[str] = UNSET
    """The resource version"""

    versionid: str
    """The UUID of the resource version"""


class ResourceEventDict(TypedDict):
    accountclientid: NotRequired[str]
    callbackurl: NotRequired[str]
    createdon: RFC3339DateTime
    description: NotRequired[str]
    deviceid: NotRequired[str]
    errmsg: NotRequired[str]
    fieldid: str
    fields: NotRequired[DtoFields | DtoFieldsDict]
    fieldvalue: NotRequired[list[int]]
    foreignid: str
    id: NotRequired[str]
    lastupdated: RFC3339DateTime
    modelid: NotRequired[str]
    name: NotRequired[str]
    sensordataaggregation: NotRequired[bool]
    state: str
    transactionid: NotRequired[str]
    version: NotRequired[str]
    versionid: str
