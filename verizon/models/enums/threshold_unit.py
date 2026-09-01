from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ThresholdUnit(str, Enum):
    """The units of the threshold. This can be KB, Kilobits, MB, Megabits, or GB, Gigabits"""

    KB = "KB"
    MB = "MB"
    GB = "GB"

    __str__ = str.__str__


ThresholdUnitOrStr: TypeAlias = Annotated[ThresholdUnit | str, open_enum_validator(ThresholdUnit)]
