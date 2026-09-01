from __future__ import annotations

from typing import TypeAlias

from ..gbiaddress_andcustomerinfo5 import GbiaddressAndcustomerinfo5, GbiaddressAndcustomerinfo5Dict
from ..gbidevice_idarray5 import GbideviceIdarray5, GbideviceIdarray5Dict

DeviceListWithServiceAddress1: TypeAlias = GbideviceIdarray5 | GbiaddressAndcustomerinfo5

DeviceListWithServiceAddress1Dict: TypeAlias = GbideviceIdarray5Dict | GbiaddressAndcustomerinfo5Dict
