from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class DataTriggerRequest(SdkBaseModel):
    comparator: Optional[str] = UNSET
    threshold: Optional[int] = UNSET
    threshold_unit: Optional[str] = Field(default=UNSET, alias="thresholdUnit")


class DataTriggerRequestDict(TypedDict):
    comparator: NotRequired[str]
    threshold: NotRequired[int]
    threshold_unit: NotRequired[str]
