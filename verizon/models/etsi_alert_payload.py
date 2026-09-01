from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .denm_payload import DenmPayload, DenmPayloadDict
from .header import Header, HeaderDict


class EtsiAlertPayload(SdkBaseModel):
    """DENM (Decentralized Environmental Notification Message) payload as defined in ETSI."""

    header: Header
    """The header of the DENM PDU."""

    denm: DenmPayload
    """The payload of the DENM PDU."""


class EtsiAlertPayloadDict(TypedDict):
    header: Header | HeaderDict
    denm: DenmPayload | DenmPayloadDict
