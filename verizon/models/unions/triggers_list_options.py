from __future__ import annotations

from typing import TypeAlias

from ..anomaly_trigger_value import AnomalyTriggerValue, AnomalyTriggerValueDict
from ..trigger_type2 import TriggerType2, TriggerType2Dict

TriggersListOptions: TypeAlias = AnomalyTriggerValue | TriggerType2

TriggersListOptionsDict: TypeAlias = AnomalyTriggerValueDict | TriggerType2Dict
