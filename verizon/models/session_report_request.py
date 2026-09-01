from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class SessionReportRequest(SdkBaseModel):
    """Request for obtaining a session report."""

    account_number: str = Field(alias="accountNumber")
    """The numeric ID of the account and must include leading zeroes. This value is indentical to ``accountName``."""

    imei: str
    """The International Mobile Equipment Identifier of the device."""

    start_date: Optional[str] = Field(default=UNSET, alias="startDate")
    """Start date of session to include. If not specified information will be shown from the earliest available (180
    days). Can be either date in ISO 8601 format or predefined constants."""

    end_date: Optional[str] = Field(default=UNSET, alias="endDate")
    """End date of session to include. If not specified information will be shown to the latest available. Can be either
    date in ISO 8601 format or predefined constants."""

    duration_low: Optional[int] = Field(default=UNSET, alias="durationLow")
    """Optional filter — minimum session duration"""

    duration_high: Optional[int] = Field(default=UNSET, alias="durationHigh")
    """Optional filter — maximum session duration"""


class SessionReportRequestDict(TypedDict):
    account_number: str
    imei: str
    start_date: NotRequired[str]
    end_date: NotRequired[str]
    duration_low: NotRequired[int]
    duration_high: NotRequired[int]
