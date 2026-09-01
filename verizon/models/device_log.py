from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import RFC3339DateTime, SdkBaseModel


class DeviceLog(SdkBaseModel):
    """Device logging information."""

    device_id: str = Field(alias="deviceId")
    """Device IMEI."""

    log_time: RFC3339DateTime = Field(alias="logTime")
    """Time of log."""

    log_type: str = Field(alias="logType")
    """Log type (one of SoftwareUpdate, Event, UserNotification, AgentService, Wireless, WirelessWeb,
    MobileBroadbandModem, WindowsMDM)."""

    event_log: str = Field(alias="eventLog")
    """Event log."""

    binary_log_file_base64: str = Field(alias="binaryLogFileBase64")
    """Base64-encoded contents of binary log file."""

    binary_log_filename: str = Field(alias="binaryLogFilename")
    """File name of binary log file."""


class DeviceLogDict(TypedDict):
    device_id: str
    log_time: RFC3339DateTime
    log_type: str
    event_log: str
    binary_log_file_base64: str
    binary_log_filename: str
