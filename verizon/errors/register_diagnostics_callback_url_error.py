from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.device_diagnostics_result import DeviceDiagnosticsResult

RegisterDiagnosticsCallbackUrlErrorBody: TypeAlias = DeviceDiagnosticsResult | RawError


@dataclass(frozen=True, slots=True)
class _RegisterDiagnosticsCallbackUrlError:
    def map(self, response: HttpResponse) -> RegisterDiagnosticsCallbackUrlErrorBody:
        match response.status_code:
            case 400:
                return decode_json[DeviceDiagnosticsResult](response)
            case _:
                return RawError(response)


register_diagnostics_callback_url_error_mapper: Final[
    ErrorMapper[RegisterDiagnosticsCallbackUrlErrorBody]
] = _RegisterDiagnosticsCallbackUrlError()
