from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class AccuracyMode(str, Enum):
    """Accurary, currently only 0-coarse supported."""

    _0 = "0"

    __str__ = str.__str__


AccuracyModeOrStr: TypeAlias = Annotated[AccuracyMode | str, open_enum_validator(AccuracyMode)]
