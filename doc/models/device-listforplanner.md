
# Device Listforplanner

## Structure

`DeviceListforplanner`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `device_ids` | [`List[DeviceIdforplanner]`](../../doc/models/device-idforplanner.md) | Optional | - |
| `private_network_apns` | [`List[PrivateNetworkApns]`](../../doc/models/private-network-apns.md) | Optional | - |
| `ipaddress` | `str` | Optional | A IPv4 address |
| `activation_code` | `str` | Optional | The activation code value. |

## Example

```python
from verizon.models.device_idforplanner import DeviceIdforplanner
from verizon.models.device_listforplanner import DeviceListforplanner
from verizon.models.private_network_apns import PrivateNetworkApns

device_listforplanner = DeviceListforplanner(
    device_ids=[
        DeviceIdforplanner(
            kind='kind8',
            id='id0'
        ),
        DeviceIdforplanner(
            kind='kind8',
            id='id0'
        ),
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
        ),
        PrivateNetworkApns(
            apn_name='apnName2',
            address_assignment_method='addressAssignmentMethod8',
            ipaddress='ipAddress4'
        )
    ],
    ipaddress='10.10.10.01',
    activation_code='activationCode4'
)
```

