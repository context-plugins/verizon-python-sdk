
# Change PWN Device Ipaddress Request

## Structure

`ChangePWNDeviceIpaddressRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `str` | Required | - |
| `device_list` | [`List[DeviceListIP]`](../../doc/models/device-list-ip.md) | Required | - |

## Example

```python
from verizon.models.change_pwn_device_ipaddress_request import ChangePWNDeviceIpaddressRequest
from verizon.models.device_list_ip import DeviceListIP
from verizon.models.pwn_device_id import PWNDeviceId

change_pwn_device_ipaddress_request = ChangePWNDeviceIpaddressRequest(
    account_name='0342351414-00001',
    device_list=[
        DeviceListIP(
            device_ids=[
                PWNDeviceId(
                    id='99948099913024600000',
                    kind='iccid'
                )
            ],
            ipaddress='10.3.4.5'
        ),
        DeviceListIP(
            device_ids=[
                PWNDeviceId(
                    id='999480500019111000001',
                    kind='iccid'
                )
            ],
            ipaddress='10.4.5.7'
        )
    ]
)
```

