from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.management_error import ManagementError
from ..models.management_error400 import ManagementError400
from ..models.management_error403 import ManagementError403
from ..models.management_error500 import ManagementError500

UpdateAprofileErrorBody: TypeAlias = (
    ManagementError400 | ManagementError | ManagementError403 | ManagementError500 | RawError
)


@dataclass(frozen=True, slots=True)
class _UpdateAprofileError:
    def map(self, response: HttpResponse) -> UpdateAprofileErrorBody:
        match response.status_code:
            case 400:
                return decode_json[ManagementError400](response)
            case 401:
                return decode_json[ManagementError](response)
            case 403:
                return decode_json[ManagementError403](response)
            case 500:
                return decode_json[ManagementError500](response)
            case _:
                return RawError(response)


update_aprofile_error_mapper: Final[ErrorMapper[UpdateAprofileErrorBody]] = _UpdateAprofileError()
