
# Change PWN Device State Deactivate Request

## Structure

`ChangePWNDeviceStateDeactivateRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `str` | Required | - |
| `device_list` | [`List[PWNDeviceList]`](../../doc/models/pwn-device-list.md) | Required | - |

## Example

```python
from verizon.models.change_pwn_device_state_deactivate_request import ChangePWNDeviceStateDeactivateRequest
from verizon.models.pwn_device_id import PWNDeviceId
from verizon.models.pwn_device_list import PWNDeviceList

change_pwn_device_state_deactivate_request = ChangePWNDeviceStateDeactivateRequest(
    account_name='0342351414-00001',
    device_list=[
        PWNDeviceList(
            device_ids=[
                PWNDeviceId(
                    id='99948099913024600000',
                    kind='iccid'
                )
            ]
        )
    ]
)
```

