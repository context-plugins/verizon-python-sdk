from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel
from .unions.keys_chunk import KeysChunk, KeysChunkDict


class Triggervalues(SdkBaseModel):
    trigger_id: Optional[str] = Field(default=UNSET, alias="triggerId")
    trigger_name: Optional[str] = Field(default=UNSET, alias="triggerName")
    account_name: Optional[str] = Field(default=UNSET, alias="accountName")
    organization_name: Optional[str] = Field(default=UNSET, alias="organizationName")
    trigger_category: Optional[str] = Field(default=UNSET, alias="triggerCategory")
    trigger_attributes: Optional[list[KeysChunk]] = Field(default=UNSET, alias="triggerAttributes")
    created_at: Optional[RFC3339DateTime] = Field(default=UNSET, alias="createdAt")
    modified_at: Optional[RFC3339DateTime] = Field(default=UNSET, alias="modifiedAt")


class TriggervaluesDict(TypedDict):
    trigger_id: NotRequired[str]
    trigger_name: NotRequired[str]
    account_name: NotRequired[str]
    organization_name: NotRequired[str]
    trigger_category: NotRequired[str]
    trigger_attributes: NotRequired[list[KeysChunk | KeysChunkDict]]
    created_at: NotRequired[RFC3339DateTime]
    modified_at: NotRequired[RFC3339DateTime]
