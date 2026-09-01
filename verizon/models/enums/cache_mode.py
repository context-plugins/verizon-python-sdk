from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class CacheMode(str, Enum):
    """Location cache mode."""

    _0 = "0"
    _1 = "1"
    _2 = "2"

    __str__ = str.__str__


CacheModeOrStr: TypeAlias = Annotated[CacheMode | str, open_enum_validator(CacheMode)]
