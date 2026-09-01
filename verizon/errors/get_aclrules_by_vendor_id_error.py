from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_text

GetAclrulesByVendorIdErrorBody: TypeAlias = str | RawError


@dataclass(frozen=True, slots=True)
class _GetAclrulesByVendorIdError:
    def map(self, response: HttpResponse) -> GetAclrulesByVendorIdErrorBody:
        match response.status_code:
            case 400 | 401 | 403 | 406 | 429:
                return decode_text[str](response)
            case _:
                return RawError(response)


get_aclrules_by_vendor_id_error_mapper: Final[
    ErrorMapper[GetAclrulesByVendorIdErrorBody]
] = _GetAclrulesByVendorIdError()
