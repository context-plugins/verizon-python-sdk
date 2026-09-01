from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .kpiinfo import Kpiinfo, KpiinfoDict


class KpiinfoList(SdkBaseModel):
    kpi_info_list: Optional[list[Kpiinfo]] = Field(default=UNSET, alias="KpiInfoList")


class KpiinfoListDict(TypedDict):
    kpi_info_list: NotRequired[list[Kpiinfo | KpiinfoDict]]
