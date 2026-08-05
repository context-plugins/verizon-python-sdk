
# Profile Change State Request

## Structure

`ProfileChangeStateRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `devices` | [`List[DeviceList]`](../../doc/models/device-list.md) | Required | - |
| `account_name` | `str` | Required | - |
| `smsr_oid` | `str` | Required | - |

## Example

```python
from verizon.models.device_id import DeviceId
from verizon.models.device_list import DeviceList
from verizon.models.profile_change_state_request import ProfileChangeStateRequest

profile_change_state_request = ProfileChangeStateRequest(
    devices=[
        DeviceList(
            device_ids=[
                DeviceId(
                    id='id0',
                    kind='kind8'
                )
            ]
        )
    ],
    account_name='1223334444-00001',
    smsr_oid='1.3.6.1.4.1.31746.1.500.200.101.5'
)
```

