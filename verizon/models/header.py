from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.message_id import MessageIdOrInt
from .enums.protocol_version import ProtocolVersionOrInt


class Header(SdkBaseModel):
    """The header of the DENM PDU."""

    protocol_version: ProtocolVersionOrInt = Field(alias="protocolVersion")
    """The protocol version of the DENM."""

    message_id: MessageIdOrInt = Field(alias="messageId")
    """The type of ITIS message (typically 1 for DENM)."""

    station_id: int = Field(alias="stationId")
    """The station identifier of the ITS-S."""


class HeaderDict(TypedDict):
    protocol_version: ProtocolVersionOrInt
    message_id: MessageIdOrInt
    station_id: int
