from __future__ import annotations

from typing import TypeAlias

from ..itisitem_wrapper import ItisitemWrapper, ItisitemWrapperDict
from ..text_item_wrapper import TextItemWrapper, TextItemWrapperDict

AdvisoryItem: TypeAlias = ItisitemWrapper | TextItemWrapper
"""The use of ITIS codes interspersed with free text. The complete set of ITIS codes can be found in Volume Two of the
SAE J2540 standard."""

AdvisoryItemDict: TypeAlias = ItisitemWrapperDict | TextItemWrapperDict
