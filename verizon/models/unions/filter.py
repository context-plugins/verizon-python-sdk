from __future__ import annotations

from typing import TypeAlias

from ..devices_filter import DevicesFilter, DevicesFilterDict
from ..pagination_filter import PaginationFilter, PaginationFilterDict

Filter: TypeAlias = DevicesFilter | PaginationFilter
"""Devices filter criteria or pagination token"""

FilterDict: TypeAlias = DevicesFilterDict | PaginationFilterDict
