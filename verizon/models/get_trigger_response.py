from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel


class GetTriggerResponse(SdkBaseModel):
    account_name: Optional[str] = Field(default=UNSET, alias="accountName")
    comparator: Optional[str] = UNSET
    created_at: Optional[RFC3339DateTime] = Field(default=UNSET, alias="createdAt")
    group_name: Optional[str] = Field(default=UNSET, alias="groupName")
    modified_at: Optional[RFC3339DateTime] = Field(default=UNSET, alias="modifiedAt")
    notification_group_name: Optional[str] = Field(default=UNSET, alias="notificationGroupName")
    organization_name: Optional[str] = Field(default=UNSET, alias="organizationName")
    sms_type: Optional[str] = Field(default=UNSET, alias="smsType")
    threshold: Optional[str] = UNSET
    threshold_unit: Optional[str] = Field(default=UNSET, alias="thresholdUnit")
    trigger_category: Optional[str] = Field(default=UNSET, alias="triggerCategory")
    trigger_cycle: Optional[str] = Field(default=UNSET, alias="triggerCycle")
    trigger_id: Optional[str] = Field(default=UNSET, alias="triggerId")
    trigger_name: Optional[str] = Field(default=UNSET, alias="triggerName")


class GetTriggerResponseDict(TypedDict):
    account_name: NotRequired[str]
    comparator: NotRequired[str]
    created_at: NotRequired[RFC3339DateTime]
    group_name: NotRequired[str]
    modified_at: NotRequired[RFC3339DateTime]
    notification_group_name: NotRequired[str]
    organization_name: NotRequired[str]
    sms_type: NotRequired[str]
    threshold: NotRequired[str]
    threshold_unit: NotRequired[str]
    trigger_category: NotRequired[str]
    trigger_cycle: NotRequired[str]
    trigger_id: NotRequired[str]
    trigger_name: NotRequired[str]
