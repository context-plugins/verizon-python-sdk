from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class SensitivityParameters(SdkBaseModel):
    """Details for sensitivity parameters."""

    abnormal_max_value: Optional[float] = Field(default=UNSET, alias="abnormalMaxValue")
    """The maximum value of the threshold in the units being measured."""

    enable_abnormal: Optional[bool] = Field(default=UNSET, alias="enableAbnormal")
    """If abnormal values are being monitored.<br />true - Monitor for abnormal values<br />false - Do not monitor for
    abnormal values."""

    enable_very_abnormal: Optional[bool] = Field(default=UNSET, alias="enableVeryAbnormal")
    """If very abnormal values are being monitored.<br />true - Monitor for very abnormal values<br />false - Do not
    monitor for very abnormal values."""

    very_abnormal_max_value: Optional[float] = Field(default=UNSET, alias="veryAbnormalMaxValue")
    """The maximum value of the threshold in the units being measured."""


class SensitivityParametersDict(TypedDict):
    abnormal_max_value: NotRequired[float]
    enable_abnormal: NotRequired[bool]
    enable_very_abnormal: NotRequired[bool]
    very_abnormal_max_value: NotRequired[float]
