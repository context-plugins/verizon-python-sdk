from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class CycleType(str, Enum):
    CYCLEONE = "cycleone"
    CYCLETWO = "cycletwo"

    __str__ = str.__str__


CycleTypeOrStr: TypeAlias = Annotated[CycleType | str, open_enum_validator(CycleType)]
