from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class AttributeIdentifier(str, Enum):
    """Attribute identifier."""

    NETWORK_BEARER = "NETWORK_BEARER"
    RADIO_SIGNAL_STRENGTH = "RADIO_SIGNAL_STRENGTH"
    LINK_QUALITY = "LINK_QUALITY"
    CELL_ID = "CELL_ID"
    MANUFACTURER = "MANUFACTURER"

    __str__ = str.__str__


AttributeIdentifierOrStr: TypeAlias = Annotated[AttributeIdentifier | str, open_enum_validator(AttributeIdentifier)]
