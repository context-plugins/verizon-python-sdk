from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class AltitudeConfidence(str, Enum):
    """Absolute accuracy of a reported altitude value. The value shall be set to:
    - 0 - ``alt-000-01`` - if the confidence value is equal to or less than 0,01 metre,
    - 1 - ``alt-000-02`` - if the confidence value is equal to or less than 0,02 metre and greater than 0,01 metre,
    - 2 - ``alt-000-05`` - if the confidence value is equal to or less than 0,05 metre and greater than 0,02 metre,
    - 3 - ``alt-000-10`` - if the confidence value is equal to or less than 0,1 metre and greater than 0,05 metre,
    - 4 - ``alt-000-20`` - if the confidence value is equal to or less than 0,2 metre and greater than 0,1 metre,
    - 5 - ``alt-000-50`` - if the confidence value is equal to or less than 0,5 metre and greater than 0,2 metre,
    - 6 - ``alt-001-00`` - if the confidence value is equal to or less than 1 metre and greater than 0,5 metre,
    - 7 - ``alt-002-00`` - if the confidence value is equal to or less than 2 metres and greater than 1 metre,
    - 8 - ``alt-005-00`` - if the confidence value is equal to or less than 5 metres and greater than 2 metres,
    - 9 - ``alt-010-00`` - if the confidence value is equal to or less than 10 metres and greater than 5 metres,
    - 10 - ``alt-020-00`` - if the confidence value is equal to or less than 20 metres and greater than 10 metres,
    - 11 - ``alt-050-00`` - if the confidence value is equal to or less than 50 metres and greater than 20 metres,
    - 12 - ``alt-100-00`` - if the confidence value is equal to or less than 100 metres and greater than 50 metres,
    - 13 - ``alt-200-00`` - if the confidence value is equal to or less than 200 metres and greater than 100 metres,
    - 14 - ``outOfRange`` - if the confidence value is out of range, i.e. greater than 200 metres,
    - 15 - ``unavailable`` - if the confidence value is unavailable."""

    ALT_000_01 = "alt-000-01"
    ALT_000_02 = "alt-000-02"
    ALT_000_05 = "alt-000-05"
    ALT_000_10 = "alt-000-10"
    ALT_000_20 = "alt-000-20"
    ALT_000_50 = "alt-000-50"
    ALT_001_00 = "alt-001-00"
    ALT_002_00 = "alt-002-00"
    ALT_005_00 = "alt-005-00"
    ALT_010_00 = "alt-010-00"
    ALT_020_00 = "alt-020-00"
    ALT_050_00 = "alt-050-00"
    ALT_100_00 = "alt-100-00"
    ALT_200_00 = "alt-200-00"
    OUT_OF_RANGE = "outOfRange"
    UNAVAILABLE = "unavailable"

    __str__ = str.__str__


AltitudeConfidenceOrStr: TypeAlias = Annotated[AltitudeConfidence | str, open_enum_validator(AltitudeConfidence)]
