from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .history_search_filter import HistorySearchFilter, HistorySearchFilterDict
from .history_search_limit_time import HistorySearchLimitTime, HistorySearchLimitTimeDict


class HistorySearchRequest(SdkBaseModel):
    """Used to filter data by time period or number of devices."""

    filter: HistorySearchFilter = Field(alias="$filter")
    """The selected device and attributes for which a request should retrieve data."""

    limit_number: Optional[int] = Field(default=UNSET, alias="$limitNumber")
    """The maximum number of historical attributes to include in the response. If the request matches more than this
    number of attributes, the response will contain an X-Next value in the header that can be used as the page value in
    the next request to retrieve the next page of events."""

    limit_time: Optional[HistorySearchLimitTime] = Field(default=UNSET, alias="$limitTime")
    """The time period for which a request should retrieve data, beginning with the limitTime.startOn and proceeding
    with the limitTime.duration."""

    page: Optional[str] = Field(default=UNSET, alias="$page")
    """Page number for pagination purposes."""


class HistorySearchRequestDict(TypedDict):
    filter: HistorySearchFilter | HistorySearchFilterDict
    limit_number: NotRequired[int]
    limit_time: NotRequired[HistorySearchLimitTime | HistorySearchLimitTimeDict]
    page: NotRequired[str]
