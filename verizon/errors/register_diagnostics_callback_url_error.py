from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.device_diagnostics_result import DeviceDiagnosticsResult

RegisterDiagnosticsCallbackUrlErrorBody: TypeAlias = DeviceDiagnosticsResult | RawError


@dataclass(frozen=True, slots=True)
class _RegisterDiagnosticsCallbackUrlError:
    def map(self, status_code: int, content: bytes) -> RegisterDiagnosticsCallbackUrlErrorBody:
        match status_code:
            case 400:
                return decode_json[DeviceDiagnosticsResult](content)
            case _:
                return RawError(status_code, content)


register_diagnostics_callback_url_error_mapper: Final[
    ErrorMapper[RegisterDiagnosticsCallbackUrlErrorBody]
] = _RegisterDiagnosticsCallbackUrlError()
