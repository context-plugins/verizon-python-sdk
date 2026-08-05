
# GIO Device Id

## Structure

`GIODeviceId`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `kind` | `str` | Required | - |
| `id` | `str` | Required | - |

## Example

```python
from verizon.models.gio_device_id import GIODeviceId

gio_device_id = GIODeviceId(
    kind='eid',
    id='12345678901234567890123456789012'
)
```

