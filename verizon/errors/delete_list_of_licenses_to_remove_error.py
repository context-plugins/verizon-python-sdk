from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError

DeleteListOfLicensesToRemoveErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _DeleteListOfLicensesToRemoveError:
    def map(self, status_code: int, content: bytes) -> DeleteListOfLicensesToRemoveErrorBody:
        match status_code:
            case 400:
                return RawError(status_code, content)
            case _:
                return RawError(status_code, content)


delete_list_of_licenses_to_remove_error_mapper: Final[
    ErrorMapper[DeleteListOfLicensesToRemoveErrorBody]
] = _DeleteListOfLicensesToRemoveError()
