from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.auth_rest_error_responseforplanner import AuthRestErrorResponseforplanner
from ..models.rest_error_responseforplanner import RestErrorResponseforplanner

StatusConnectionPlannerErrorBody: TypeAlias = RestErrorResponseforplanner | AuthRestErrorResponseforplanner | RawError


@dataclass(frozen=True, slots=True)
class _StatusConnectionPlannerError:
    def map(self, response: HttpResponse) -> StatusConnectionPlannerErrorBody:
        match response.status_code:
            case 400 | 403 | 404 | 406 | 429:
                return decode_json[RestErrorResponseforplanner](response)
            case 401:
                return decode_json[AuthRestErrorResponseforplanner](response)
            case _:
                return RawError(response)


status_connection_planner_error_mapper: Final[
    ErrorMapper[StatusConnectionPlannerErrorBody]
] = _StatusConnectionPlannerError()
