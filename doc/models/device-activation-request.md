
# Device Activation Request

Request for device status to check availability of activation.

## Structure

`DeviceActivationRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `str` | Required | The name of a billing account. |
| `devices` | [`List[AccountDeviceList]`](../../doc/models/account-device-list.md) | Required | Up to 10,000 devices that you want to move to a different account, specified by device identifier. |

## Example

```python
from verizon.models.account_device_list import AccountDeviceList
from verizon.models.device_activation_request import DeviceActivationRequest
from verizon.models.device_id import DeviceId

device_activation_request = DeviceActivationRequest(
    account_name='0212345678-00001',
    devices=[
        AccountDeviceList(
            device_ids=[
                DeviceId(
                    id='15-digit IMEI',
                    kind='imei'
                )
            ],
            ipaddress='ipAddress4'
        )
    ]
)
```

