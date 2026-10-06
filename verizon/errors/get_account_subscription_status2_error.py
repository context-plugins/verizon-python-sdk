from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.fota_v2_result import FotaV2Result

GetAccountSubscriptionStatus2ErrorBody: TypeAlias = FotaV2Result | RawError


@dataclass(frozen=True, slots=True)
class _GetAccountSubscriptionStatus2Error:
    def map(self, status_code: int, content: bytes) -> GetAccountSubscriptionStatus2ErrorBody:
        match status_code:
            case 400:
                return decode_json[FotaV2Result](content)
            case _:
                return RawError(status_code, content)


get_account_subscription_status2_error_mapper: Final[
    ErrorMapper[GetAccountSubscriptionStatus2ErrorBody]
] = _GetAccountSubscriptionStatus2Error()
