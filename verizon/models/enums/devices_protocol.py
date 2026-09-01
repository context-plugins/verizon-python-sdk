from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class DevicesProtocol(str, Enum):
    """Firmware protocol. Valid values include: LWM2M, OMADM, HTTP."""

    LWM2_M = "LWM2M"
    OMDADM = "OMDADM"
    HTTP = "HTTP"

    __str__ = str.__str__


DevicesProtocolOrStr: TypeAlias = Annotated[DevicesProtocol | str, open_enum_validator(DevicesProtocol)]
