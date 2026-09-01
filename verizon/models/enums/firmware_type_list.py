from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class FirmwareTypeList(str, Enum):
    """Possible values are ``append`` or ``remove``"""

    APPEND = "append"
    REMOVE = "remove"

    __str__ = str.__str__


FirmwareTypeListOrStr: TypeAlias = Annotated[FirmwareTypeList | str, open_enum_validator(FirmwareTypeList)]
