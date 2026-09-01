from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .devicepropertyfilter import Devicepropertyfilter, DevicepropertyfilterDict


class ResourceResourceQuery(SdkBaseModel):
    filter: Optional[Devicepropertyfilter] = UNSET


class ResourceResourceQueryDict(TypedDict):
    filter: NotRequired[Devicepropertyfilter | DevicepropertyfilterDict]
