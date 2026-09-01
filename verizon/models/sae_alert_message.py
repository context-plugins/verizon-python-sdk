from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .sae_alert_payload import SaeAlertPayload, SaeAlertPayloadDict


class SaeAlertMessage(SdkBaseModel):
    """Road Side Alert (RSA) message and its mandatory fields. This message is used to send alerts for nearby hazards to
    travelers. This message is defined in the SAE J2735 Standard. The system supports all mandatory fields, but only a
    subset of the optional fields."""

    sae_alert: SaeAlertPayload = Field(alias="saeAlert")
    """Road Side Alert (RSA) message payload as defined in SAE J2735."""


class SaeAlertMessageDict(TypedDict):
    sae_alert: SaeAlertPayload | SaeAlertPayloadDict
