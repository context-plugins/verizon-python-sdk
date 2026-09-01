from __future__ import annotations

from typing import TypeAlias

from ..data_percentage50_trigger_attribute import DataPercentage50TriggerAttribute, DataPercentage50TriggerAttributeDict
from ..data_percentage75_trigger_attribute import DataPercentage75TriggerAttribute, DataPercentage75TriggerAttributeDict
from ..data_percentage90_trigger_attribute import DataPercentage90TriggerAttribute, DataPercentage90TriggerAttributeDict
from ..data_percentage100_trigger_attribute import (
    DataPercentage100TriggerAttribute,
    DataPercentage100TriggerAttributeDict,
)
from ..notification_group_name_trigger_attribute import (
    NotificationGroupNameTriggerAttribute,
    NotificationGroupNameTriggerAttributeDict,
)
from ..service_plan_trigger_attribute import ServicePlanTriggerAttribute, ServicePlanTriggerAttributeDict

TriggerAttributes: TypeAlias = (
    NotificationGroupNameTriggerAttribute
    | ServicePlanTriggerAttribute
    | DataPercentage50TriggerAttribute
    | DataPercentage75TriggerAttribute
    | DataPercentage90TriggerAttribute
    | DataPercentage100TriggerAttribute
)

TriggerAttributesDict: TypeAlias = (
    NotificationGroupNameTriggerAttributeDict
    | ServicePlanTriggerAttributeDict
    | DataPercentage50TriggerAttributeDict
    | DataPercentage75TriggerAttributeDict
    | DataPercentage90TriggerAttributeDict
    | DataPercentage100TriggerAttributeDict
)
