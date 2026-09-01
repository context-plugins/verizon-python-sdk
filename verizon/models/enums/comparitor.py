from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Comparitor(str, Enum):
    """The boolean of the comparison. ``gt`` is Greater Than, ``lt`` is Less Than and ``eq`` is Equal To"""

    GT = "gt"
    LT = "lt"
    EQ = "eq"

    __str__ = str.__str__


ComparitorOrStr: TypeAlias = Annotated[Comparitor | str, open_enum_validator(Comparitor)]
