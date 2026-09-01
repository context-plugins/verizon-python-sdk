from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .unions.trigger_attributes_options import TriggerAttributesOptions, TriggerAttributesOptionsDict


class AnomalyTriggerValue(SdkBaseModel):
    """Trigger details."""

    trigger_id: Optional[str] = Field(default=UNSET, alias="triggerId")
    """The system assigned name of the trigger being updated."""

    trigger_name: Optional[str] = Field(default=UNSET, alias="triggerName")
    """The user defined name of the trigger."""

    organization_name: Optional[str] = Field(default=UNSET, alias="organizationName")
    """The user assigned name of the organization associated with the trigger."""

    trigger_category: Optional[str] = Field(default=UNSET, alias="triggerCategory")
    """This is the value to use in the request body to detect anomalous behaivior. The values in this table will only be
    relevant when this parameter is set to this value."""

    trigger_attributes: Optional[list[TriggerAttributesOptions]] = Field(default=UNSET, alias="triggerAttributes")
    """Additional details and keys for the trigger."""

    created_at: Optional[str] = Field(default=UNSET, alias="createdAt")
    """Timestamp for whe the trigger was created."""

    modified_at: Optional[str] = Field(default=UNSET, alias="modifiedAt")
    """Timestamp for the most recent time the trigger was modified."""


class AnomalyTriggerValueDict(TypedDict):
    trigger_id: NotRequired[str]
    trigger_name: NotRequired[str]
    organization_name: NotRequired[str]
    trigger_category: NotRequired[str]
    trigger_attributes: NotRequired[list[TriggerAttributesOptions | TriggerAttributesOptionsDict]]
    created_at: NotRequired[str]
    modified_at: NotRequired[str]
