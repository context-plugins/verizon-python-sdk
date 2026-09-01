from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Devicepropertyselection(SdkBaseModel):
    modelid: Optional[str] = UNSET


class DevicepropertyselectionDict(TypedDict):
    modelid: NotRequired[str]
