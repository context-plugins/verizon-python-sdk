from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class MessageId(int, Enum):
    """The type of ITIS message (typically 1 for DENM)."""

    VALUE_1 = 1
    """Value 1 — identifies the message as a DENM"""

    __str__ = str.__str__


MessageIdOrInt: TypeAlias = Annotated[MessageId | int, open_enum_validator(MessageId)]
