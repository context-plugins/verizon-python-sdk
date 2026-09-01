from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .filter_criteria1 import FilterCriteria1, FilterCriteria1Dict


class FiltercriteriaObjectCall(SdkBaseModel):
    filter_criteria: Optional[FilterCriteria1] = Field(default=UNSET, alias="filterCriteria")


class FiltercriteriaObjectCallDict(TypedDict):
    filter_criteria: NotRequired[FilterCriteria1 | FilterCriteria1Dict]
