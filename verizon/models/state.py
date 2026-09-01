from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class State(SdkBaseModel):
    """Each service includes custom states."""

    name: Optional[str] = UNSET
    """The name of the state."""

    workflow_sequence_number: Optional[float] = Field(default=UNSET, alias="workflowSequenceNumber")
    """The workflow sequence number of this state."""

    service_plans: Optional[list[str]] = Field(default=UNSET, alias="servicePlans")
    """The service plans that can be used to charge for services for devices in this state."""


class StateDict(TypedDict):
    name: NotRequired[str]
    workflow_sequence_number: NotRequired[float]
    service_plans: NotRequired[list[str]]
