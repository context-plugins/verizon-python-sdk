from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.intelligence_result import IntelligenceResult

CreateAnomalyDetectionTriggerErrorBody: TypeAlias = IntelligenceResult | RawError


@dataclass(frozen=True, slots=True)
class _CreateAnomalyDetectionTriggerError:
    def map(self, status_code: int, content: bytes) -> CreateAnomalyDetectionTriggerErrorBody:
        match status_code:
            case 400 | 401 | 403 | 404 | 406 | 429:
                return decode_json[IntelligenceResult](content)
            case _:
                return RawError(status_code, content)


create_anomaly_detection_trigger_error_mapper: Final[
    ErrorMapper[CreateAnomalyDetectionTriggerErrorBody]
] = _CreateAnomalyDetectionTriggerError()
