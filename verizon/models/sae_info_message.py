from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .sae_info_payload import SaeInfoPayload, SaeInfoPayloadDict


class SaeInfoMessage(SdkBaseModel):
    """Traveler Information Message (TIM) message and its mandatory fields. The traveler information message is used to
    send various types of information (advisory and road sign types) to equipped devices."""

    sae_info: SaeInfoPayload = Field(alias="saeInfo")
    """Traveler Information Message (TIM) payload as defined in SAE J2735."""


class SaeInfoMessageDict(TypedDict):
    sae_info: SaeInfoPayload | SaeInfoPayloadDict
