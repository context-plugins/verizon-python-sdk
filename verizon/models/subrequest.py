from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .giodevice_id import GiodeviceId, GiodeviceIdDict


class Subrequest(SdkBaseModel):
    ids: Optional[GiodeviceId] = UNSET
    status: Optional[str] = UNSET


class SubrequestDict(TypedDict):
    ids: NotRequired[GiodeviceId | GiodeviceIdDict]
    status: NotRequired[str]
