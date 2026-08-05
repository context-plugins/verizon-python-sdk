
# PWN Device List

## Structure

`PWNDeviceList`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `device_ids` | [`List[PWNDeviceId]`](../../doc/models/pwn-device-id.md) | Required | - |

## Example

```python
from verizon.models.pwn_device_id import PWNDeviceId
from verizon.models.pwn_device_list import PWNDeviceList

pwn_device_list = PWNDeviceList(
    device_ids=[
        PWNDeviceId(
            id='99948099913024600001',
            kind='iccid'
        )
    ]
)
```

