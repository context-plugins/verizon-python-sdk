from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .sensitivity_parameters import SensitivityParameters, SensitivityParametersDict


class AnomalyDetectionSettings(SdkBaseModel):
    """Settings for anomaly detection."""

    account_name: Optional[str] = Field(default=UNSET, alias="accountName")
    """Indicates if the account name used has anomaly detection.<br />Success - The account has anomaly detection.<br
    />Failure - The account does not have anomaly detection."""

    sensitivity_parameter: Optional[SensitivityParameters] = Field(default=UNSET, alias="sensitivityParameter")
    """Details for sensitivity parameters."""

    status: Optional[str] = UNSET
    """Indicates if anomaly detection is active on the account<br />Active - Anomaly detection is active<br />Disabled-
    Anomaly detection is not active."""


class AnomalyDetectionSettingsDict(TypedDict):
    account_name: NotRequired[str]
    sensitivity_parameter: NotRequired[SensitivityParameters | SensitivityParametersDict]
    status: NotRequired[str]
