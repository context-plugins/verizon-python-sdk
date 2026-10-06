from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_text

GetAclrulesByVendorIdErrorBody: TypeAlias = str | RawError


@dataclass(frozen=True, slots=True)
class _GetAclrulesByVendorIdError:
    def map(self, status_code: int, content: bytes) -> GetAclrulesByVendorIdErrorBody:
        match status_code:
            case 400 | 401 | 403 | 406 | 429:
                return decode_text[str](content)
            case _:
                return RawError(status_code, content)


get_aclrules_by_vendor_id_error_mapper: Final[
    ErrorMapper[GetAclrulesByVendorIdErrorBody]
] = _GetAclrulesByVendorIdError()
