from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.report_status import ReportStatusOrStr


class AsynchronousLocationRequestResult(SdkBaseModel):
    txid: Optional[str] = UNSET
    """The transaction ID of the report."""

    status: Optional[ReportStatusOrStr] = UNSET
    """Status of the report."""

    estimated_duration: Optional[str] = Field(default=UNSET, alias="estimatedDuration")
    """Estimated number of minutes required to complete the report."""


class AsynchronousLocationRequestResultDict(TypedDict):
    txid: NotRequired[str]
    status: NotRequired[ReportStatusOrStr]
    estimated_duration: NotRequired[str]
