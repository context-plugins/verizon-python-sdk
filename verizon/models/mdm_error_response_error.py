from __future__ import annotations

from uuid import UUID

from typing_extensions import TypedDict

from ..core import RFC3339DateTime, SdkBaseModel


class MdmErrorResponseError(SdkBaseModel):
    """error response structure"""

    error: str
    """The short summary of the error"""

    description: str
    """The detailed description of the error"""

    uuid: UUID
    """The unique identifier of the request for tracing"""

    timestamp: RFC3339DateTime
    """The timestamp of when the error occurred"""


class MdmErrorResponseErrorDict(TypedDict):
    error: str
    description: str
    uuid: UUID
    timestamp: RFC3339DateTime
