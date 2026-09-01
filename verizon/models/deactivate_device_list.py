from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .unions.id import Id, IdDict


class DeactivateDeviceList(SdkBaseModel):
    ids: Optional[list[Id]] = UNSET


class DeactivateDeviceListDict(TypedDict):
    ids: NotRequired[list[Id | IdDict]]
