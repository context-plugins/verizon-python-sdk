from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.fota_v2_result import FotaV2Result

UploadConfigFileErrorBody: TypeAlias = FotaV2Result | RawError


@dataclass(frozen=True, slots=True)
class _UploadConfigFileError:
    def map(self, response: HttpResponse) -> UploadConfigFileErrorBody:
        match response.status_code:
            case 400:
                return decode_json[FotaV2Result](response)
            case _:
                return RawError(response)


upload_config_file_error_mapper: Final[ErrorMapper[UploadConfigFileErrorBody]] = _UploadConfigFileError()
