from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class EtxrespondingError(SdkBaseModel):
    """error response structure"""

    error: str
    """The short summary of the error"""

    description: str
    """The detailed description of the error"""


class EtxrespondingErrorDict(TypedDict):
    error: str
    description: str
