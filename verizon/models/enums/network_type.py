from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class NetworkType(str, Enum):
    """The type of the device's network connection at the time of the request. If the device is on the Verizon cellular
    network it should use the "VZ" value otherwise the "non-VZ" value.

    Devices on the Verizon network can directly access the ETX Message Exchange on the MEC (Mobile Edge Compute
    server)"""

    VZ = "VZ"
    NON_VZ = "non-VZ"

    __str__ = str.__str__


NetworkTypeOrStr: TypeAlias = Annotated[NetworkType | str, open_enum_validator(NetworkType)]
