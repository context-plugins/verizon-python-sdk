from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class MessageStandard(str, Enum):
    """Select which V2X messaging standard will be used for the message generation. The following options are supported:
      - "etsi": The message will be generated using the ETSI (European) standard (e.g. DENM).
      - "sae": The message will be generated using the SAE J2735 (North American) standard (e.g. RSA, TIM).
      - if not sent while POST, defaults to "sae"
      - mandatory to send "etsi" standard here, if ETSI messages are being sent in config"""

    ETSI = "etsi"
    SAE = "sae"

    __str__ = str.__str__


MessageStandardOrStr: TypeAlias = Annotated[MessageStandard | str, open_enum_validator(MessageStandard)]
