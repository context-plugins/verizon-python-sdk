from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .generic_payload import GenericPayload, GenericPayloadDict


class GenericMessage(SdkBaseModel):
    """A message carrying a generic (custom) V2X payload."""

    generic: GenericPayload
    """Custom message which is defined by the user and can support "any" message type or format.

    **Note:** ETX prefers the j2735 or the j2735_gr encoding and only vendor specific message types are allowed to be
    published in different message formats."""


class GenericMessageDict(TypedDict):
    generic: GenericPayload | GenericPayloadDict
