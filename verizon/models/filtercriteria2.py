from __future__ import annotations

from typing import Any

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Filtercriteria2(SdkBaseModel):
    filter_criteria: Optional[list[Any]] = Field(default=UNSET, alias="filterCriteria")


class Filtercriteria2Dict(TypedDict):
    filter_criteria: NotRequired[list[Any]]
