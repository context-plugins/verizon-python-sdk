
# Device List IP

## Structure

`DeviceListIP`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `device_ids` | [`List[PWNDeviceId]`](../../doc/models/pwn-device-id.md) | Required | - |
| `ipaddress` | `str` | Required | - |

## Example

```python
from verizon.models.device_list_ip import DeviceListIP
from verizon.models.pwn_device_id import PWNDeviceId

device_list_ip = DeviceListIP(
    device_ids=[
        PWNDeviceId(
            id='99948099913024600000',
            kind='iccid'
        )
    ],
    ipaddress='10.3.4.5'
)
```

