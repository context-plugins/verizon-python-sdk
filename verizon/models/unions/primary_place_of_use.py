from __future__ import annotations

from typing import TypeAlias

from ..addressquery import Addressquery, AddressqueryDict
from ..customernamequery import Customernamequery, CustomernamequeryDict

PrimaryPlaceOfUse: TypeAlias = Customernamequery | Addressquery

PrimaryPlaceOfUseDict: TypeAlias = CustomernamequeryDict | AddressqueryDict
