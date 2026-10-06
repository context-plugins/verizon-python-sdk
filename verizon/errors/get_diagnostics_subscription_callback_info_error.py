from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.device_diagnostics_result import DeviceDiagnosticsResult

GetDiagnosticsSubscriptionCallbackInfoErrorBody: TypeAlias = DeviceDiagnosticsResult | RawError


@dataclass(frozen=True, slots=True)
class _GetDiagnosticsSubscriptionCallbackInfoError:
    def map(self, status_code: int, content: bytes) -> GetDiagnosticsSubscriptionCallbackInfoErrorBody:
        match status_code:
            case 400:
                return decode_json[DeviceDiagnosticsResult](content)
            case _:
                return RawError(status_code, content)


get_diagnostics_subscription_callback_info_error_mapper: Final[
    ErrorMapper[GetDiagnosticsSubscriptionCallbackInfoErrorBody]
] = _GetDiagnosticsSubscriptionCallbackInfoError()
