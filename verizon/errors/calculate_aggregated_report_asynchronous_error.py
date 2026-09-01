from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.hyper_precise_location_result import HyperPreciseLocationResult

CalculateAggregatedReportAsynchronousErrorBody: TypeAlias = HyperPreciseLocationResult | RawError


@dataclass(frozen=True, slots=True)
class _CalculateAggregatedReportAsynchronousError:
    def map(self, response: HttpResponse) -> CalculateAggregatedReportAsynchronousErrorBody:
        match response.status_code:
            case 400 | 401 | 403 | 404 | 409 | 500:
                return decode_json[HyperPreciseLocationResult](response)
            case _:
                return RawError(response)


calculate_aggregated_report_asynchronous_error_mapper: Final[
    ErrorMapper[CalculateAggregatedReportAsynchronousErrorBody]
] = _CalculateAggregatedReportAsynchronousError()
