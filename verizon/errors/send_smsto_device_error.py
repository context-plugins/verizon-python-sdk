from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.connectivity_management_result import ConnectivityManagementResult

SendSmstoDeviceErrorBody: TypeAlias = ConnectivityManagementResult | RawError


@dataclass(frozen=True, slots=True)
class _SendSmstoDeviceError:
    def map(self, status_code: int, content: bytes) -> SendSmstoDeviceErrorBody:
        match status_code:
            case 400:
                return decode_json[ConnectivityManagementResult](content)
            case _:
                return RawError(status_code, content)


send_smsto_device_error_mapper: Final[ErrorMapper[SendSmstoDeviceErrorBody]] = _SendSmstoDeviceError()
