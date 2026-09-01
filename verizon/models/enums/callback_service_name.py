from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class CallbackServiceName(str, Enum):
    """The name of the callback service."""

    LOCATION = "Location"
    DEVICE_LOCATION = "DeviceLocation"

    __str__ = str.__str__


CallbackServiceNameOrStr: TypeAlias = Annotated[CallbackServiceName | str, open_enum_validator(CallbackServiceName)]
