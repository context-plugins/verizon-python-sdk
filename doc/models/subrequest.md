
# Subrequest

## Structure

`Subrequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `ids` | [`GIODeviceId`](../../doc/models/gio-device-id.md) | Optional | - |
| `status` | `str` | Optional | **Constraints**: *Minimum Length*: `3`, *Maximum Length*: `8`, *Pattern*: `^[A-Za-z]{3,8}$` |

## Example

```python
from verizon.models.gio_device_id import GIODeviceId
from verizon.models.subrequest import Subrequest

subrequest = Subrequest(
    ids=GIODeviceId(
        kind='kind2',
        id='id4'
    ),
    status='Success'
)
```

