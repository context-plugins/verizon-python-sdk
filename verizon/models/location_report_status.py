from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.report_status import ReportStatusOrStr


class LocationReportStatus(SdkBaseModel):
    """Status of the report."""

    txid: Optional[str] = UNSET
    """The transaction ID of the report."""

    status: Optional[ReportStatusOrStr] = UNSET
    """Status of the report."""


class LocationReportStatusDict(TypedDict):
    txid: NotRequired[str]
    status: NotRequired[ReportStatusOrStr]
