from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class FirmwareProtocol(str, Enum):
    """Firmware protocol. Valid values include: LWM2M, OMD-DM, all."""

    LWM2_M = "LWM2M"
    OMD_DM = "OMD-DM"
    ALL = "all"

    __str__ = str.__str__


FirmwareProtocolOrStr: TypeAlias = Annotated[FirmwareProtocol | str, open_enum_validator(FirmwareProtocol)]
