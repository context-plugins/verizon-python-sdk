from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.intelligence_result import IntelligenceResult

ListAnomalyDetectionTriggerSettingsErrorBody: TypeAlias = IntelligenceResult | RawError


@dataclass(frozen=True, slots=True)
class _ListAnomalyDetectionTriggerSettingsError:
    def map(self, status_code: int, content: bytes) -> ListAnomalyDetectionTriggerSettingsErrorBody:
        match status_code:
            case 400 | 401 | 403 | 404 | 406 | 429:
                return decode_json[IntelligenceResult](content)
            case _:
                return RawError(status_code, content)


list_anomaly_detection_trigger_settings_error_mapper: Final[
    ErrorMapper[ListAnomalyDetectionTriggerSettingsErrorBody]
] = _ListAnomalyDetectionTriggerSettingsError()
