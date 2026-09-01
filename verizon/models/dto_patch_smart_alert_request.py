from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .dto_resourceidentifier import DtoResourceidentifier, DtoResourceidentifierDict
from .user_smart_alert import UserSmartAlert, UserSmartAlertDict


class DtoPatchSmartAlertRequest(SdkBaseModel):
    accountname: Optional[str] = UNSET
    """The numeric account name, which must include leading zeros"""

    resourceidentifier: Optional[DtoResourceidentifier] = UNSET
    smartalert: Optional[UserSmartAlert] = UNSET


class DtoPatchSmartAlertRequestDict(TypedDict):
    accountname: NotRequired[str]
    resourceidentifier: NotRequired[DtoResourceidentifier | DtoResourceidentifierDict]
    smartalert: NotRequired[UserSmartAlert | UserSmartAlertDict]
