from __future__ import annotations

from typing import TypeAlias

from ..gbiattribute15 import Gbiattribute15, Gbiattribute15Dict
from ..gbiattribute25 import Gbiattribute25, Gbiattribute25Dict

ExtendedAttribute: TypeAlias = Gbiattribute15 | Gbiattribute25 | Gbiattribute15 | Gbiattribute25 | Gbiattribute15

ExtendedAttributeDict: TypeAlias = (
    Gbiattribute15Dict | Gbiattribute25Dict | Gbiattribute15Dict | Gbiattribute25Dict | Gbiattribute15Dict
)
