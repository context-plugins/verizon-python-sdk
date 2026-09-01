from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .etsi_alert_payload import EtsiAlertPayload, EtsiAlertPayloadDict


class EtsiAlertMessage(SdkBaseModel):
    """Decentralized Environmental Notification Message (DENM) message and its mandatory fields. It is used in order to
    alert road users of a detected event using ITS communication technologies."""

    etsi_alert: EtsiAlertPayload = Field(alias="etsiAlert")
    """DENM (Decentralized Environmental Notification Message) payload as defined in ETSI."""


class EtsiAlertMessageDict(TypedDict):
    etsi_alert: EtsiAlertPayload | EtsiAlertPayloadDict
