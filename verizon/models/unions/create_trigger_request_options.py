from __future__ import annotations

from typing import TypeAlias

from ..active_anomaly_indicator import ActiveAnomalyIndicator, ActiveAnomalyIndicatorDict
from ..active_trigger_indicator import ActiveTriggerIndicator, ActiveTriggerIndicatorDict
from ..trigger_type1 import TriggerType1, TriggerType1Dict

CreateTriggerRequestOptions: TypeAlias = TriggerType1 | ActiveAnomalyIndicator | ActiveTriggerIndicator

CreateTriggerRequestOptionsDict: TypeAlias = TriggerType1Dict | ActiveAnomalyIndicatorDict | ActiveTriggerIndicatorDict
