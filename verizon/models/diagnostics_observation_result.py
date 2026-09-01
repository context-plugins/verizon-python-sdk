from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import RFC3339DateTime, SdkBaseModel


class DiagnosticsObservationResult(SdkBaseModel):
    """A success response containing the current status of the request."""

    transaction_id: str = Field(alias="transactionID")
    """Transaction identifier."""

    status: str
    """Status of the request."""

    created_on: RFC3339DateTime = Field(alias="createdOn")
    """The date and time of when this request was created."""


class DiagnosticsObservationResultDict(TypedDict):
    transaction_id: str
    status: str
    created_on: RFC3339DateTime
