from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.connectivity_management_result import ConnectivityManagementResult

SendSmstoDeviceErrorBody: TypeAlias = ConnectivityManagementResult | RawError


@dataclass(frozen=True, slots=True)
class _SendSmstoDeviceError:
    def map(self, response: HttpResponse) -> SendSmstoDeviceErrorBody:
        match response.status_code:
            case 400:
                return decode_json[ConnectivityManagementResult](response)
            case _:
                return RawError(response)


send_smsto_device_error_mapper: Final[ErrorMapper[SendSmstoDeviceErrorBody]] = _SendSmstoDeviceError()
