from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .pay_as_you_go_filter_criteria1 import PayAsYouGoFilterCriteria1, PayAsYouGoFilterCriteria1Dict


class PayAsYouGoFilterCriteria(SdkBaseModel):
    filter_criteria: Optional[PayAsYouGoFilterCriteria1] = Field(default=UNSET, alias="filterCriteria")


class PayAsYouGoFilterCriteriaDict(TypedDict):
    filter_criteria: NotRequired[PayAsYouGoFilterCriteria1 | PayAsYouGoFilterCriteria1Dict]
