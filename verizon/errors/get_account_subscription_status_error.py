from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.fota_v1_result import FotaV1Result

GetAccountSubscriptionStatusErrorBody: TypeAlias = FotaV1Result | RawError


@dataclass(frozen=True, slots=True)
class _GetAccountSubscriptionStatusError:
    def map(self, response: HttpResponse) -> GetAccountSubscriptionStatusErrorBody:
        match response.status_code:
            case 400:
                return decode_json[FotaV1Result](response)
            case _:
                return RawError(response)


get_account_subscription_status_error_mapper: Final[
    ErrorMapper[GetAccountSubscriptionStatusErrorBody]
] = _GetAccountSubscriptionStatusError()
