from __future__ import annotations

from typing import Any

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class SensorInsightsBle(SdkBaseModel):
    """Property objects for Bluetooth Low-Energy (BLE) devices"""

    data_mode: Optional[int] = Field(default=UNSET, alias="dataMode")
    """The data mode the sensor is using"""

    manufacturer_id: Optional[int] = Field(default=UNSET, alias="manufacturerId")
    """The numeric manufacturer ID"""

    max_num_scan: Optional[int] = Field(default=UNSET, alias="maxNumScan")
    """How frequently the device can be scanned"""

    min_sig_str: Optional[int] = Field(default=UNSET, alias="minSigStr")
    """The minimum signal strength needed for the sensor to transmit (in Decibels or dB)"""

    monitor_period: Optional[int] = Field(default=UNSET, alias="monitorPeriod")
    """The ammount of time to monitor the sensor and varies by device"""

    more_manuf_id: Optional[list[Any]] = Field(default=UNSET, alias="moreManufId")
    """Values for the manufacturer and these vary by device"""

    op_mode: Optional[int] = Field(default=UNSET, alias="opMode")
    """The operation mode"""

    report_offset: Optional[int] = Field(default=UNSET, alias="reportOffset")
    """The ammount of time between sensor readings and reports"""

    report_period: Optional[int] = Field(default=UNSET, alias="reportPeriod")
    """The ammount of time between reports"""

    report_type: Optional[int] = Field(default=UNSET, alias="reportType")
    """The report type"""

    scan_duration: Optional[int] = Field(default=UNSET, alias="scanDuration")
    """The ammount of time the sensor is queried for data"""


class SensorInsightsBleDict(TypedDict):
    data_mode: NotRequired[int]
    manufacturer_id: NotRequired[int]
    max_num_scan: NotRequired[int]
    min_sig_str: NotRequired[int]
    monitor_period: NotRequired[int]
    more_manuf_id: NotRequired[list[Any]]
    op_mode: NotRequired[int]
    report_offset: NotRequired[int]
    report_period: NotRequired[int]
    report_type: NotRequired[int]
    scan_duration: NotRequired[int]
