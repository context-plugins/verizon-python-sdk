from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .sensitivity_parameters import SensitivityParameters, SensitivityParametersDict


class AnomalyDetectionRequest(SdkBaseModel):
    """Anomaly detection request."""

    account_name: Optional[str] = Field(default=UNSET, alias="accountName")
    """The name of a billing account. An account name is usually numeric, and must include any leading zeros."""

    request_type: Optional[str] = Field(default=UNSET, alias="requestType")
    """The type of request being made. anomaly is the request to activate anomaly detection."""

    sensitivity_parameter: Optional[SensitivityParameters] = Field(default=UNSET, alias="sensitivityParameter")
    """Details for sensitivity parameters."""


class AnomalyDetectionRequestDict(TypedDict):
    account_name: NotRequired[str]
    request_type: NotRequired[str]
    sensitivity_parameter: NotRequired[SensitivityParameters | SensitivityParametersDict]
