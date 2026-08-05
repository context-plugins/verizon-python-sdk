
# Change PWN Device State Activate Request

## Structure

`ChangePWNDeviceStateActivateRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `str` | Required | - |
| `device_list` | [`List[PWNDeviceList]`](../../doc/models/pwn-device-list.md) | Required | - |
| `activate` | [`Activate`](../../doc/models/activate.md) | Required | - |

## Example

```python
from verizon.models.activate import Activate
from verizon.models.change_pwn_device_state_activate_request import ChangePWNDeviceStateActivateRequest
from verizon.models.pwn_device_id import PWNDeviceId
from verizon.models.pwn_device_list import PWNDeviceList

change_pwn_device_state_activate_request = ChangePWNDeviceStateActivateRequest(
    account_name='0342351414-00001',
    device_list=[
        PWNDeviceList(
            device_ids=[
                PWNDeviceId(
                    id='99948099913024600001',
                    kind='iccid'
                )
            ]
        )
    ],
    activate=Activate(
        profile='HSS EsmProfile Enterprise 5G'
    )
)
```

