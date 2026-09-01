from __future__ import annotations

from typing import Any

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class EtxMapDataIngestRequest(SdkBaseModel):
    """JSON representation of a J2735/ETSI MapData message for ingestion. The value field must contain a valid MAP
    message body conforming to the SAE J2735 or ETSI TS 103 301 standard."""

    message_id: int = Field(alias="messageId")
    """SAE J2735 DSRCmsgID for the MAP message type."""

    value: Any
    """The decoded MAP message body containing intersection and lane data."""

    msg_issue_revision: Optional[int] = Field(default=UNSET, alias="msgIssueRevision")
    """Issue revision number of the MAP message."""


class EtxMapDataIngestRequestDict(TypedDict):
    message_id: int
    value: Any
    msg_issue_revision: NotRequired[int]
