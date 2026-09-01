from __future__ import annotations

from typing import TypeAlias

from ..cellphonenumber import Cellphonenumber, CellphonenumberDict

SmsNumberModel: TypeAlias = Cellphonenumber | Cellphonenumber

SmsNumberModelDict: TypeAlias = CellphonenumberDict | CellphonenumberDict
