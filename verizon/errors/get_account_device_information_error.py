from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.fota_v3_result import FotaV3Result

GetAccountDeviceInformationErrorBody: TypeAlias = FotaV3Result | RawError


@dataclass(frozen=True, slots=True)
class _GetAccountDeviceInformationError:
    def map(self, response: HttpResponse) -> GetAccountDeviceInformationErrorBody:
        match response.status_code:
            case 400:
                return decode_json[FotaV3Result](response)
            case _:
                return RawError(response)


get_account_device_information_error_mapper: Final[
    ErrorMapper[GetAccountDeviceInformationErrorBody]
] = _GetAccountDeviceInformationError()
