from __future__ import annotations

from typing import TypeAlias

from ..active_anomaly_indicator import ActiveAnomalyIndicator, ActiveAnomalyIndicatorDict
from ..trigger_type3 import TriggerType3, TriggerType3Dict

UpdateV2TriggerRequest: TypeAlias = TriggerType3 | ActiveAnomalyIndicator

UpdateV2TriggerRequestDict: TypeAlias = TriggerType3Dict | ActiveAnomalyIndicatorDict
