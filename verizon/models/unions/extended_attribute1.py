from __future__ import annotations

from typing import TypeAlias

from ..gbiattribute15 import Gbiattribute15, Gbiattribute15Dict
from ..gbiattribute25 import Gbiattribute25, Gbiattribute25Dict

ExtendedAttribute1: TypeAlias = Gbiattribute15 | Gbiattribute25 | Gbiattribute15 | Gbiattribute25 | Gbiattribute15

ExtendedAttribute1Dict: TypeAlias = (
    Gbiattribute15Dict | Gbiattribute25Dict | Gbiattribute15Dict | Gbiattribute25Dict | Gbiattribute15Dict
)
