from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.connectivity_management_result import ConnectivityManagementResult

GetDeviceExtendedDiagnosticInformationErrorBody: TypeAlias = ConnectivityManagementResult | RawError


@dataclass(frozen=True, slots=True)
class _GetDeviceExtendedDiagnosticInformationError:
    def map(self, status_code: int, content: bytes) -> GetDeviceExtendedDiagnosticInformationErrorBody:
        match status_code:
            case 400:
                return decode_json[ConnectivityManagementResult](content)
            case _:
                return RawError(status_code, content)


get_device_extended_diagnostic_information_error_mapper: Final[
    ErrorMapper[GetDeviceExtendedDiagnosticInformationErrorBody]
] = _GetDeviceExtendedDiagnosticInformationError()
