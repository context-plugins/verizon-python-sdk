from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.connectivity_management_result import ConnectivityManagementResult

GetDeviceExtendedDiagnosticInformationErrorBody: TypeAlias = ConnectivityManagementResult | RawError


@dataclass(frozen=True, slots=True)
class _GetDeviceExtendedDiagnosticInformationError:
    def map(self, response: HttpResponse) -> GetDeviceExtendedDiagnosticInformationErrorBody:
        match response.status_code:
            case 400:
                return decode_json[ConnectivityManagementResult](response)
            case _:
                return RawError(response)


get_device_extended_diagnostic_information_error_mapper: Final[
    ErrorMapper[GetDeviceExtendedDiagnosticInformationErrorBody]
] = _GetDeviceExtendedDiagnosticInformationError()
