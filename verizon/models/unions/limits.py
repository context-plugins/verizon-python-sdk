from __future__ import annotations

from typing import TypeAlias

from ..heading_item import HeadingItem, HeadingItemDict
from ..speed_item import SpeedItem, SpeedItemDict

Limits: TypeAlias = SpeedItem | HeadingItem

LimitsDict: TypeAlias = SpeedItemDict | HeadingItemDict
