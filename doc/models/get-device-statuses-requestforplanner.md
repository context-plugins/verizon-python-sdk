
# Get Device Statuses Requestforplanner

## Structure

`GetDeviceStatusesRequestforplanner`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_number` | `str` | Optional | The numeric name of the account, including leading zeros. |
| `request_id` | `str` | Optional | The unique ID of a request. This is a UUID value. |
| `devices` | [`List[DeviceListforplanner]`](../../doc/models/device-listforplanner.md) | Optional | - |

## Example

```python
from verizon.models.device_idforplanner import DeviceIdforplanner
from verizon.models.device_listforplanner import DeviceListforplanner
from verizon.models.get_device_statuses_requestforplanner import GetDeviceStatusesRequestforplanner
from verizon.models.private_network_apns import PrivateNetworkApns

get_device_statuses_requestforplanner = GetDeviceStatusesRequestforplanner(
    account_number='0000123456-00001',
    request_id='d24cc6e4-eeee-ffff-gggg-0ffbb091c076',
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
        ),
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

