from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class CallbackService(str, Enum):
    """Callback type. Must be 'Fota' for Software Management Services API."""

    FOTA = "Fota"

    __str__ = str.__str__


CallbackServiceOrStr: TypeAlias = Annotated[CallbackService | str, open_enum_validator(CallbackService)]
