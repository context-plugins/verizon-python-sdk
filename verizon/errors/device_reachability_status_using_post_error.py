from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.connectivity_management_result import ConnectivityManagementResult

DeviceReachabilityStatusUsingPostErrorBody: TypeAlias = ConnectivityManagementResult | RawError


@dataclass(frozen=True, slots=True)
class _DeviceReachabilityStatusUsingPostError:
    def map(self, response: HttpResponse) -> DeviceReachabilityStatusUsingPostErrorBody:
        match response.status_code:
            case 400:
                return decode_json[ConnectivityManagementResult](response)
            case _:
                return RawError(response)


device_reachability_status_using_post_error_mapper: Final[
    ErrorMapper[DeviceReachabilityStatusUsingPostErrorBody]
] = _DeviceReachabilityStatusUsingPostError()
