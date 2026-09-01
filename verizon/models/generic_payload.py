from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class GenericPayload(SdkBaseModel):
    """Custom message which is defined by the user and can support "any" message type or format.

    **Note:** ETX prefers the j2735 or the j2735_gr encoding and only vendor specific message types are allowed to be
    published in different message formats."""

    message_type: str = Field(alias="messageType")
    """The type of message. This can be any of the standard V2X messages specified in the SAE J2735 standard (e.g. BSM,
    PSM, RSA, TIM, MAP, SPAT, etc.), or it can be a vendor specific message type that is not defined by the standard."""

    message_format: str = Field(alias="messageFormat")
    """The encoding of the message (e.g. j2735, protobuf, json, Avro, etc.). If the message is encapsulated within a
    GeoRoutedMsg protocol buffer wrapper, append _gr to the message format (e.g. j2735 => j2735_gr).

    **Note:** ETX prefers the j2735 or the j2735_gr encoding and only vendor specific message types are allowed to be
    published in different message formats."""

    payload: str
    """The base64 encoded message."""


class GenericPayloadDict(TypedDict):
    message_type: str
    message_format: str
    payload: str
