from __future__ import annotations

from typing import TypeAlias

from ..gbiaddress_andcustomerinfo25 import GbiaddressAndcustomerinfo25, GbiaddressAndcustomerinfo25Dict
from ..gbidevice_idarray25 import GbideviceIdarray25, GbideviceIdarray25Dict

DeviceListWithServiceAddress: TypeAlias = GbideviceIdarray25 | GbiaddressAndcustomerinfo25

DeviceListWithServiceAddressDict: TypeAlias = GbideviceIdarray25Dict | GbiaddressAndcustomerinfo25Dict
