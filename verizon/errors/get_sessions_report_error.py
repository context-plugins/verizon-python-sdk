from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.hyper_precise_location_result import HyperPreciseLocationResult

GetSessionsReportErrorBody: TypeAlias = HyperPreciseLocationResult | RawError


@dataclass(frozen=True, slots=True)
class _GetSessionsReportError:
    def map(self, status_code: int, content: bytes) -> GetSessionsReportErrorBody:
        match status_code:
            case 400 | 401 | 403 | 404 | 409 | 500:
                return decode_json[HyperPreciseLocationResult](content)
            case _:
                return RawError(status_code, content)


get_sessions_report_error_mapper: Final[ErrorMapper[GetSessionsReportErrorBody]] = _GetSessionsReportError()
