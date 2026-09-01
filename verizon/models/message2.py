from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .distribution_schedule import DistributionSchedule, DistributionScheduleDict
from .enums.distribution_types import DistributionTypesOrStr
from .enums.road_user_types import RoadUserTypesOrStr
from .enums.trigger_condition import TriggerConditionOrStr
from .sae_info_payload import SaeInfoPayload, SaeInfoPayloadDict
from .unions.limit import Limit, LimitDict


class Message2(SdkBaseModel):
    is_private: bool = Field(alias="isPrivate")
    """Defines whether the message is private or public. Private messages are published under the Vendor ID defined in
    the configuration and only visible to devices of selected vendors. Public messages are published under the Public
    vendor and are visible to all the users."""

    road_user_type: list[RoadUserTypesOrStr] = Field(alias="roadUserType")
    """Type of the Road User."""

    trigger_conditions: list[TriggerConditionOrStr] = Field(alias="triggerConditions")
    """Trigger conditions that define on which road user action the message will be sent. If multiple Trigger Conditions
    are defined any of them will trigger the message."""

    limits: Optional[list[Limit]] = UNSET
    """List of limitations. These limitations can be used for making the trigger condition more precise by defining
    speed and motion direction requirements to be met before the messages are sent out."""

    distribution_type: Optional[list[DistributionTypesOrStr]] = Field(default=UNSET, alias="distributionType")
    """Type of the distribution."""

    distribution_schedule: Optional[DistributionSchedule] = Field(default=UNSET, alias="distributionSchedule")
    """The distribution schedule parameters for broadcast messages."""

    sae_info: SaeInfoPayload = Field(alias="saeInfo")
    """Traveler Information Message (TIM) payload as defined in SAE J2735."""


class Message2Dict(TypedDict):
    is_private: bool
    road_user_type: list[RoadUserTypesOrStr]
    trigger_conditions: list[TriggerConditionOrStr]
    limits: NotRequired[list[Limit | LimitDict]]
    distribution_type: NotRequired[list[DistributionTypesOrStr]]
    distribution_schedule: NotRequired[DistributionSchedule | DistributionScheduleDict]
    sae_info: SaeInfoPayload | SaeInfoPayloadDict
