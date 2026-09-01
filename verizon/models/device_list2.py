from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .unions.id1 import Id1, Id1Dict


class DeviceList2(SdkBaseModel):
    ids: Optional[list[Id1]] = UNSET


class DeviceList2Dict(TypedDict):
    ids: NotRequired[list[Id1 | Id1Dict]]
