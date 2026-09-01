from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class PaginationFilter(SdkBaseModel):
    """Pagination filter containing an opaque token for fetching the next/previous page of results. The page token is
    returned in the response headers (X-Next, X-Prev) and should be passed as-is."""

    page: str = Field(alias="Page")
    """Opaque pagination token for fetching the next/previous page of results. This is a encoded string. Do not parse or
    modify; pass it as received."""


class PaginationFilterDict(TypedDict):
    page: str
