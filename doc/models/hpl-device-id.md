
# Hpl Device Id

Identifier object pairs of kind/id

## Structure

`HplDeviceId`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `kind` | `str` | Optional | The type of ID. This can be IMEI or ICCID. |
| `id` | `str` | Optional | The ID value. |

## Example

```python
from verizon.models.hpl_device_id import HplDeviceId

hpl_device_id = HplDeviceId(
    kind='kind8',
    id='id0'
)
```

