from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .custom_fields import CustomFields, CustomFieldsDict


class ProvisioningHistory(SdkBaseModel):
    """The provisioning history of a specified device during a specified time period."""

    occurred_at: Optional[str] = Field(default=UNSET, alias="occurredAt")
    """The date and time when the provisioning event occured."""

    status: Optional[str] = UNSET
    """The success or failure of the provisioning event."""

    event_by: Optional[str] = Field(default=UNSET, alias="eventBy")
    """The user who performed the provisioning event."""

    event_type: Optional[str] = Field(default=UNSET, alias="eventType")
    """The provisioning action:Activate,Suspend,Restore,Deactivate,Device Move."""

    mdn: Optional[str] = UNSET
    """The MDN assigned to the device after the provisioning event."""

    msisdn: Optional[str] = UNSET
    """The MSISDN assigned to the device after the provisioning event."""

    service_plan: Optional[str] = Field(default=UNSET, alias="servicePlan")
    """The service plan of the device after the provisioning event occurred."""

    extended_attributes: Optional[list[CustomFields]] = Field(default=UNSET, alias="extendedAttributes")
    """Any extended attributes for the event, as Key and Value pairs."""


class ProvisioningHistoryDict(TypedDict):
    occurred_at: NotRequired[str]
    status: NotRequired[str]
    event_by: NotRequired[str]
    event_type: NotRequired[str]
    mdn: NotRequired[str]
    msisdn: NotRequired[str]
    service_plan: NotRequired[str]
    extended_attributes: NotRequired[list[CustomFields | CustomFieldsDict]]
