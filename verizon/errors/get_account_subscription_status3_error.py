from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.fota_v3_result import FotaV3Result

GetAccountSubscriptionStatus3ErrorBody: TypeAlias = FotaV3Result | RawError


@dataclass(frozen=True, slots=True)
class _GetAccountSubscriptionStatus3Error:
    def map(self, status_code: int, content: bytes) -> GetAccountSubscriptionStatus3ErrorBody:
        match status_code:
            case 400:
                return decode_json[FotaV3Result](content)
            case _:
                return RawError(status_code, content)


get_account_subscription_status3_error_mapper: Final[
    ErrorMapper[GetAccountSubscriptionStatus3ErrorBody]
] = _GetAccountSubscriptionStatus3Error()
