from __future__ import annotations

from typing import TypeAlias

from ..heading_item import HeadingItem, HeadingItemDict
from ..speed_item import SpeedItem, SpeedItemDict

Limit: TypeAlias = SpeedItem | HeadingItem

LimitDict: TypeAlias = SpeedItemDict | HeadingItemDict
