
# Get Devices Windows Requestforplanner

## Structure

`GetDevicesWindowsRequestforplanner`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_number` | `str` | Optional | The numeric name of the account, including leading zeros. |
| `filter` | `str` | Optional | what windows to filter for: All - all 24 windows in a day, Best - top 3 windows by RAN KPI, Worst - lowest 3 windows by RAN KPI |
| `devices` | [`List[DeviceListforplanner]`](../../doc/models/device-listforplanner.md) | Optional | - |

## Example

```python
from verizon.models.device_idforplanner import DeviceIdforplanner
from verizon.models.device_listforplanner import DeviceListforplanner
from verizon.models.get_devices_windows_requestforplanner import GetDevicesWindowsRequestforplanner
from verizon.models.private_network_apns import PrivateNetworkApns

get_devices_windows_requestforplanner = GetDevicesWindowsRequestforplanner(
    account_number='0000123456-00001',
    filter='filter8',
    devices=[
        DeviceListforplanner(
            device_ids=[
                DeviceIdforplanner(
                    kind='kind8',
                    id='id0'
                )
            ],
            private_network_apns=[
                PrivateNetworkApns(
                    apn_name='apnName2',
                    address_assignment_method='addressAssignmentMethod8',
                    ipaddress='ipAddress4'
                ),
                PrivateNetworkApns(
                    apn_name='apnName2',
                    address_assignment_method='addressAssignmentMethod8',
                    ipaddress='ipAddress4'
                )
            ],
            ipaddress='ipAddress4',
            activation_code='activationCode2'
        )
    ]
)
```

