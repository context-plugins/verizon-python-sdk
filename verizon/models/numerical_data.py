from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.numerical_data_unit import NumericalDataUnitOrStr


class NumericalData(SdkBaseModel):
    """Describes value and unit of time."""

    value: Optional[int] = UNSET
    """Numerical value."""

    unit: Optional[NumericalDataUnitOrStr] = UNSET
    """Unit of time."""


class NumericalDataDict(TypedDict):
    value: NotRequired[int]
    unit: NotRequired[NumericalDataUnitOrStr]
