from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.auth_rest_error_responseforplanner import AuthRestErrorResponseforplanner
from ..models.rest_error_responseforplanner import RestErrorResponseforplanner

GetAccountInformationUsingGetErrorBody: TypeAlias = (
    RestErrorResponseforplanner | AuthRestErrorResponseforplanner | RawError
)


@dataclass(frozen=True, slots=True)
class _GetAccountInformationUsingGetError:
    def map(self, status_code: int, content: bytes) -> GetAccountInformationUsingGetErrorBody:
        match status_code:
            case 400 | 403 | 404 | 406 | 429:
                return decode_json[RestErrorResponseforplanner](content)
            case 401:
                return decode_json[AuthRestErrorResponseforplanner](content)
            case _:
                return RawError(status_code, content)


get_account_information_using_get_error_mapper: Final[
    ErrorMapper[GetAccountInformationUsingGetErrorBody]
] = _GetAccountInformationUsingGetError()
