from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Type12(str, Enum):
    """Indicates the type of ice."""

    SMOOTH = "smooth"

    __str__ = str.__str__


Type12OrStr: TypeAlias = Annotated[Type12 | str, open_enum_validator(Type12)]
