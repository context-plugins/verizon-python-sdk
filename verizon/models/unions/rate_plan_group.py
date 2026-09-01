from __future__ import annotations

from typing import TypeAlias

from ..rateplantype2 import Rateplantype2, Rateplantype2Dict
from ..rateplantype_object import RateplantypeObject, RateplantypeObjectDict

RatePlanGroup: TypeAlias = RateplantypeObject | Rateplantype2

RatePlanGroupDict: TypeAlias = RateplantypeObjectDict | Rateplantype2Dict
