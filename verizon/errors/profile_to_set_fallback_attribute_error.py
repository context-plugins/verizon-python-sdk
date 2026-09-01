from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.rest_error_response import RestErrorResponse

ProfileToSetFallbackAttributeErrorBody: TypeAlias = RestErrorResponse | RawError


@dataclass(frozen=True, slots=True)
class _ProfileToSetFallbackAttributeError:
    def map(self, response: HttpResponse) -> ProfileToSetFallbackAttributeErrorBody:
        match response.status_code:
            case 400:
                return decode_json[RestErrorResponse](response)
            case _:
                return RawError(response)


profile_to_set_fallback_attribute_error_mapper: Final[
    ErrorMapper[ProfileToSetFallbackAttributeErrorBody]
] = _ProfileToSetFallbackAttributeError()
