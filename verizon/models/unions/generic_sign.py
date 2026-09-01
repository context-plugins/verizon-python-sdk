from __future__ import annotations

from typing import TypeAlias

from ..itisitem_wrapper import ItisitemWrapper, ItisitemWrapperDict
from ..text_phrase_item_wrapper import TextPhraseItemWrapper, TextPhraseItemWrapperDict

GenericSign: TypeAlias = ItisitemWrapper | TextPhraseItemWrapper
"""A data frame to allow sequences of ITIS codes, short text strings, and numerical values to be expressed in the normal
ITIS vocabulary method and pattern. Note that the allowed text strings are more limited than the normal ITIS format in
order to conserve bandwidth."""

GenericSignDict: TypeAlias = ItisitemWrapperDict | TextPhraseItemWrapperDict
