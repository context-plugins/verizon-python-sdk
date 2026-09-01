from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class RulesCycleType(str, Enum):
    """The interval to monitor for the threshold. This can be Daily, Weekly or Monthly"""

    DAILY = "Daily"
    WEEKLY = "Weekly"
    MONTHLY = "Monthly"

    __str__ = str.__str__


RulesCycleTypeOrStr: TypeAlias = Annotated[RulesCycleType | str, open_enum_validator(RulesCycleType)]
