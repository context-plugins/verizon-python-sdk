from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.hyper_precise_location_result import HyperPreciseLocationResult

CalculateAggregatedReportSynchronousErrorBody: TypeAlias = HyperPreciseLocationResult | RawError


@dataclass(frozen=True, slots=True)
class _CalculateAggregatedReportSynchronousError:
    def map(self, response: HttpResponse) -> CalculateAggregatedReportSynchronousErrorBody:
        match response.status_code:
            case 400 | 401 | 403 | 404 | 409 | 500:
                return decode_json[HyperPreciseLocationResult](response)
            case _:
                return RawError(response)


calculate_aggregated_report_synchronous_error_mapper: Final[
    ErrorMapper[CalculateAggregatedReportSynchronousErrorBody]
] = _CalculateAggregatedReportSynchronousError()
