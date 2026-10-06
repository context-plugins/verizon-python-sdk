from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.connectivity_management_result import ConnectivityManagementResult

GetDeviceGroupInformationErrorBody: TypeAlias = ConnectivityManagementResult | RawError


@dataclass(frozen=True, slots=True)
class _GetDeviceGroupInformationError:
    def map(self, status_code: int, content: bytes) -> GetDeviceGroupInformationErrorBody:
        match status_code:
            case 400:
                return decode_json[ConnectivityManagementResult](content)
            case _:
                return RawError(status_code, content)


get_device_group_information_error_mapper: Final[
    ErrorMapper[GetDeviceGroupInformationErrorBody]
] = _GetDeviceGroupInformationError()
