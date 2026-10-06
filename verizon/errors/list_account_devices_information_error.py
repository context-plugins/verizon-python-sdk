from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.fota_v3_result import FotaV3Result

ListAccountDevicesInformationErrorBody: TypeAlias = FotaV3Result | RawError


@dataclass(frozen=True, slots=True)
class _ListAccountDevicesInformationError:
    def map(self, status_code: int, content: bytes) -> ListAccountDevicesInformationErrorBody:
        match status_code:
            case 400:
                return decode_json[FotaV3Result](content)
            case _:
                return RawError(status_code, content)


list_account_devices_information_error_mapper: Final[
    ErrorMapper[ListAccountDevicesInformationErrorBody]
] = _ListAccountDevicesInformationError()
