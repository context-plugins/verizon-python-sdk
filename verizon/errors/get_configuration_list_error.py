from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.response_error import ResponseError

GetConfigurationListErrorBody: TypeAlias = ResponseError | RawError


@dataclass(frozen=True, slots=True)
class _GetConfigurationListError:
    def map(self, response: HttpResponse) -> GetConfigurationListErrorBody:
        match response.status_code:
            case 403 | 404 | 429:
                return decode_json[ResponseError](response)
            case _:
                return RawError(response)


get_configuration_list_error_mapper: Final[ErrorMapper[GetConfigurationListErrorBody]] = _GetConfigurationListError()
