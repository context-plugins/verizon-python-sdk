from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.connectivity_management_result import ConnectivityManagementResult

UpdateDevicesCustomFieldsErrorBody: TypeAlias = ConnectivityManagementResult | RawError


@dataclass(frozen=True, slots=True)
class _UpdateDevicesCustomFieldsError:
    def map(self, status_code: int, content: bytes) -> UpdateDevicesCustomFieldsErrorBody:
        match status_code:
            case 400:
                return decode_json[ConnectivityManagementResult](content)
            case _:
                return RawError(status_code, content)


update_devices_custom_fields_error_mapper: Final[
    ErrorMapper[UpdateDevicesCustomFieldsErrorBody]
] = _UpdateDevicesCustomFieldsError()
