from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class AggregateSessionReportRequest(SdkBaseModel):
    """Request for getting an aggregated session report."""

    account_number: str = Field(alias="accountNumber")
    """The numeric ID of the account and must include leading zeroes. This value is indentical to ``accountName``."""

    start_date: Optional[str] = Field(default=UNSET, alias="startDate")
    """Start date of session to include. If not specified information will be shown from the earliest available (180
    days). Can be either date in ISO 8601 format or predefined constants."""

    end_date: Optional[str] = Field(default=UNSET, alias="endDate")
    """End date of session to include. If not specified information will be shown to the latest available. Can be either
    date in ISO 8601 format or predefined constants."""

    imei: list[str]
    """Devices for which return usage info. Could be 0, 1 or more. In case of 0 will return all devices belonging to
    customer (except of filtered by other parameters)."""

    device_group: Optional[str] = Field(default=UNSET, alias="deviceGroup")
    """Optional filter — only include devices matching this device group name."""

    data_plan: Optional[str] = Field(default=UNSET, alias="dataPlan")
    """Optional filter — only include devices matching this carrier rate plan code."""

    no_session_flag: Optional[bool] = Field(default=UNSET, alias="noSessionFlag")
    """Optional filter — when "true", returns only devices with no sessions."""


class AggregateSessionReportRequestDict(TypedDict):
    account_number: str
    start_date: NotRequired[str]
    end_date: NotRequired[str]
    imei: list[str]
    device_group: NotRequired[str]
    data_plan: NotRequired[str]
    no_session_flag: NotRequired[bool]
