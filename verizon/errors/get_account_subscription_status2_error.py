from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.fota_v2_result import FotaV2Result

GetAccountSubscriptionStatus2ErrorBody: TypeAlias = FotaV2Result | RawError


@dataclass(frozen=True, slots=True)
class _GetAccountSubscriptionStatus2Error:
    def map(self, response: HttpResponse) -> GetAccountSubscriptionStatus2ErrorBody:
        match response.status_code:
            case 400:
                return decode_json[FotaV2Result](response)
            case _:
                return RawError(response)


get_account_subscription_status2_error_mapper: Final[
    ErrorMapper[GetAccountSubscriptionStatus2ErrorBody]
] = _GetAccountSubscriptionStatus2Error()
