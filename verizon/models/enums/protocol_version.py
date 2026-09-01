from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ProtocolVersion(int, Enum):
    """The protocol version of the DENM."""

    VALUE_2 = 2
    """Version 2 — current DENM PDU protocol version"""

    __str__ = str.__str__


ProtocolVersionOrInt: TypeAlias = Annotated[ProtocolVersion | int, open_enum_validator(ProtocolVersion)]
