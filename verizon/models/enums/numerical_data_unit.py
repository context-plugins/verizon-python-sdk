from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class NumericalDataUnit(str, Enum):
    """Unit of time."""

    SECOND = "SECOND"
    MINUTE = "MINUTE"
    HOUR = "HOUR"
    DAY = "DAY"

    __str__ = str.__str__


NumericalDataUnitOrStr: TypeAlias = Annotated[NumericalDataUnit | str, open_enum_validator(NumericalDataUnit)]
