from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class EtxexpectedTypeEnum(str, Enum):
    """The format of the payload in the response body."""

    BASE64 = "BASE64"
    JSON = "JSON"

    __str__ = str.__str__


EtxexpectedTypeEnumOrStr: TypeAlias = Annotated[EtxexpectedTypeEnum | str, open_enum_validator(EtxexpectedTypeEnum)]
