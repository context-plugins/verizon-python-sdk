from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.report_status import ReportStatusOrStr


class SynchronousLocationRequestResult(SdkBaseModel):
    txid: str
    """The transaction ID of the report."""

    status: ReportStatusOrStr
    """Status of the report."""


class SynchronousLocationRequestResultDict(TypedDict):
    txid: str
    status: ReportStatusOrStr
