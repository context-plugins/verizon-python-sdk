from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class UsageAnomalyAttributes(SdkBaseModel):
    """The details of the UsageAnomaly trigger."""

    account_names: Optional[str] = Field(default=UNSET, alias="accountNames")
    """The Verizon billing account associated with the anomaly triggers for this trigger to be active for devices in
    those accounts. An account name is usually numeric, and must include any leading zeros."""

    device_group: Optional[str] = Field(default=UNSET, alias="deviceGroup")
    """The names of device groups associated with the anomaly triggers for this trigger to be active for devices in
    those groups."""

    include_abnormal: Optional[bool] = Field(default=UNSET, alias="includeAbnormal")
    """Whether or not to include anomalies classified as 'abnormal'.<br />true<br />false<br />Classification is set as
    part of ThingSpace Intelligence anomaly detection settings."""

    include_very_abnormal: Optional[bool] = Field(default=UNSET, alias="includeVeryAbnormal")
    """Whether or not to include anomalies classified as 'very abnormal'.<br />true<br />false<br />Classification is
    set as part of ThingSpace Intelligence anomaly detection settings."""

    include_under_expected_usage: Optional[bool] = Field(default=UNSET, alias="includeUnderExpectedUsage")
    """Whether or not to include anomalies that are directionally under the expected usage.<br />true<br />false."""

    include_over_expected_usage: Optional[bool] = Field(default=UNSET, alias="includeOverExpectedUsage")
    """Whether or not to include anomalies that are directionally over the expected usage. <br />true<br />false."""


class UsageAnomalyAttributesDict(TypedDict):
    account_names: NotRequired[str]
    device_group: NotRequired[str]
    include_abnormal: NotRequired[bool]
    include_very_abnormal: NotRequired[bool]
    include_under_expected_usage: NotRequired[bool]
    include_over_expected_usage: NotRequired[bool]
