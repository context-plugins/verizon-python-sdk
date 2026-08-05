
# Device

Identifies a particular IoT device.

## Structure

`Device`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Required | Device identifier. |
| `kind` | `str` | Required | Device kind identifier. |

## Example

```python
from verizon.models.device import Device

device = Device(
    id='864508030026238',
    kind='IMEI'
)
```

