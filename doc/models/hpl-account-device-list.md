
# Hpl Account Device List

A list of device IDs

## Structure

`HplAccountDeviceList`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `device_ids` | [`List[HplDeviceId]`](../../doc/models/hpl-device-id.md) | Optional | - |

## Example

```python
from verizon.models.hpl_account_device_list import HplAccountDeviceList
from verizon.models.hpl_device_id import HplDeviceId

hpl_account_device_list = HplAccountDeviceList(
    device_ids=[
        HplDeviceId(
            kind='kind8',
            id='id0'
        ),
        HplDeviceId(
            kind='kind8',
            id='id0'
        )
    ]
)
```

