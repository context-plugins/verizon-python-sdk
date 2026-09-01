from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ServiceName(str, Enum):
    """Service name"""

    LOCATION = "Location"
    FOTA = "fota"

    __str__ = str.__str__


ServiceNameOrStr: TypeAlias = Annotated[ServiceName | str, open_enum_validator(ServiceName)]
