from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.fota_v2_result import FotaV2Result

GetListOfFilesErrorBody: TypeAlias = FotaV2Result | RawError


@dataclass(frozen=True, slots=True)
class _GetListOfFilesError:
    def map(self, response: HttpResponse) -> GetListOfFilesErrorBody:
        match response.status_code:
            case 400:
                return decode_json[FotaV2Result](response)
            case _:
                return RawError(response)


get_list_of_files_error_mapper: Final[ErrorMapper[GetListOfFilesErrorBody]] = _GetListOfFilesError()
