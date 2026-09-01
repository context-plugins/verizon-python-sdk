from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ConditionType(str, Enum):
    """The condition type being monitored"""

    INDIVIDUAL = "Individual"
    AGING = "Aging"
    USAGE_ALLOWANCE = "UsageAllowance"

    __str__ = str.__str__


ConditionTypeOrStr: TypeAlias = Annotated[ConditionType | str, open_enum_validator(ConditionType)]
