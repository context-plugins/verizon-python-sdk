from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Type8(str, Enum):
    """Indicates the type of gravel."""

    PACKED_OILED = "packedOiled"
    LOOSE = "loose"

    __str__ = str.__str__


Type8OrStr: TypeAlias = Annotated[Type8 | str, open_enum_validator(Type8)]
