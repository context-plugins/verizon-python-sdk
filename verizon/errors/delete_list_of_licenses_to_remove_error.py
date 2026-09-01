from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError

DeleteListOfLicensesToRemoveErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _DeleteListOfLicensesToRemoveError:
    def map(self, response: HttpResponse) -> DeleteListOfLicensesToRemoveErrorBody:
        match response.status_code:
            case 400:
                return RawError(response)
            case _:
                return RawError(response)


delete_list_of_licenses_to_remove_error_mapper: Final[
    ErrorMapper[DeleteListOfLicensesToRemoveErrorBody]
] = _DeleteListOfLicensesToRemoveError()
