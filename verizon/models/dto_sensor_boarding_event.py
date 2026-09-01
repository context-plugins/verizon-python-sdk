from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel
from .dto_fields import DtoFields, DtoFieldsDict


class DtoSensorBoardingEvent(SdkBaseModel):
    createdon: Optional[RFC3339DateTime] = UNSET
    """Timestamp of the record"""

    errmsg: Optional[str] = UNSET
    """Error message"""

    fields: Optional[DtoFields] = UNSET
    """Fields to return needed by search"""

    state: Optional[str] = UNSET
    """The current status of the device or transaction and will be ``success`` or ``failed``"""

    transactionid: Optional[str] = UNSET
    """The system-generated UUID of the transaction"""


class DtoSensorBoardingEventDict(TypedDict):
    createdon: NotRequired[RFC3339DateTime]
    errmsg: NotRequired[str]
    fields: NotRequired[DtoFields | DtoFieldsDict]
    state: NotRequired[str]
    transactionid: NotRequired[str]
