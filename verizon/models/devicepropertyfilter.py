from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .devicepropertyselection import Devicepropertyselection, DevicepropertyselectionDict


class Devicepropertyfilter(SdkBaseModel):
    selection: Optional[Devicepropertyselection] = Field(default=UNSET, alias="$selection")
    querytotalcount: Optional[bool] = Field(default=UNSET, alias="$querytotalcount")


class DevicepropertyfilterDict(TypedDict):
    selection: NotRequired[Devicepropertyselection | DevicepropertyselectionDict]
    querytotalcount: NotRequired[bool]
