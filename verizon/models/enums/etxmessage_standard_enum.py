from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class EtxmessageStandardEnum(str, Enum):
    """V2X messaging standard selection. Accepted values are 'sae' (SAE J2735) and 'etsi' (ETSI TS 103 301)."""

    ETSI = "etsi"
    SAE = "sae"

    __str__ = str.__str__


EtxmessageStandardEnumOrStr: TypeAlias = Annotated[
    EtxmessageStandardEnum | str, open_enum_validator(EtxmessageStandardEnum)
]
