from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.intelligence_result import IntelligenceResult

UpdateAnomalyDetectionTriggerErrorBody: TypeAlias = IntelligenceResult | RawError


@dataclass(frozen=True, slots=True)
class _UpdateAnomalyDetectionTriggerError:
    def map(self, response: HttpResponse) -> UpdateAnomalyDetectionTriggerErrorBody:
        match response.status_code:
            case 400 | 401 | 403 | 404 | 406 | 429:
                return decode_json[IntelligenceResult](response)
            case _:
                return RawError(response)


update_anomaly_detection_trigger_error_mapper: Final[
    ErrorMapper[UpdateAnomalyDetectionTriggerErrorBody]
] = _UpdateAnomalyDetectionTriggerError()
