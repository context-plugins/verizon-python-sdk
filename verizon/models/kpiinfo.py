from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Kpiinfo(SdkBaseModel):
    """KPI Info Object"""

    name: Optional[str] = UNSET
    value: Optional[str] = UNSET
    node_name: Optional[str] = Field(default=UNSET, alias="nodeName")
    node_type: Optional[str] = Field(default=UNSET, alias="nodeType")
    description: Optional[str] = UNSET
    unit: Optional[str] = UNSET
    category: Optional[str] = UNSET
    time_of_last_update: Optional[str] = Field(default=UNSET, alias="timeOfLastUpdate")


class KpiinfoDict(TypedDict):
    name: NotRequired[str]
    value: NotRequired[str]
    node_name: NotRequired[str]
    node_type: NotRequired[str]
    description: NotRequired[str]
    unit: NotRequired[str]
    category: NotRequired[str]
    time_of_last_update: NotRequired[str]
