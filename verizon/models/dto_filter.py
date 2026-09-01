from __future__ import annotations

from typing import Any

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class DtoFilter(SdkBaseModel):
    expand: Optional[str] = Field(default=UNSET, alias="$expand")
    """Use to provide device details for alerts specific to a device"""

    limitnumber: Optional[int] = Field(default=UNSET, alias="$limitnumber")
    """Limit the number of results returned"""

    nopagination: Optional[bool] = Field(default=UNSET, alias="$nopagination")
    """A flag set to show if pagination requested (false) or not (true)"""

    page: Optional[str] = Field(default=UNSET, alias="$page")
    pagenumber: Optional[int] = Field(default=UNSET, alias="$pagenumber")
    projection: Optional[list[str]] = Field(default=UNSET, alias="$projection")
    """Limits the fields of the device that the user is interested in rather than all of the fields"""

    selection: Optional[dict[str, Any]] = Field(default=UNSET, alias="$selection")
    """Filters results based on user defined criteria"""


class DtoFilterDict(TypedDict):
    expand: NotRequired[str]
    limitnumber: NotRequired[int]
    nopagination: NotRequired[bool]
    page: NotRequired[str]
    pagenumber: NotRequired[int]
    projection: NotRequired[list[str]]
    selection: NotRequired[dict[str, Any]]
