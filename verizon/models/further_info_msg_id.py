from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class FurtherInfoMsgId(SdkBaseModel):
    """Message ID referencing a further information link (ATIS message)."""

    further_info_id: str = Field(alias="furtherInfoID")
    """Links to ATIS message. A link to any other incident information data that may be available in the normal ATIS
    incident description or other messages.

    The value is described as a 4-character hexadecimal string."""


class FurtherInfoMsgIdDict(TypedDict):
    further_info_id: str
