from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.device_diagnostics_result import DeviceDiagnosticsResult

UnregisterDiagnosticsCallbackErrorBody: TypeAlias = DeviceDiagnosticsResult | RawError


@dataclass(frozen=True, slots=True)
class _UnregisterDiagnosticsCallbackError:
    def map(self, response: HttpResponse) -> UnregisterDiagnosticsCallbackErrorBody:
        match response.status_code:
            case 400:
                return decode_json[DeviceDiagnosticsResult](response)
            case _:
                return RawError(response)


unregister_diagnostics_callback_error_mapper: Final[
    ErrorMapper[UnregisterDiagnosticsCallbackErrorBody]
] = _UnregisterDiagnosticsCallbackError()
