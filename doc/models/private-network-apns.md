
# Private Network Apns

## Structure

`PrivateNetworkApns`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `apn_name` | `str` | Optional | the Access Point Name |
| `address_assignment_method` | `str` | Optional | The method used for address assignment. |
| `ipaddress` | `str` | Optional | A IPv4 address |

## Example

```python
from verizon.models.private_network_apns import PrivateNetworkApns

private_network_apns = PrivateNetworkApns(
    apn_name='apnName8',
    address_assignment_method='addressAssignmentMethod4',
    ipaddress='10.10.10.01'
)
```

