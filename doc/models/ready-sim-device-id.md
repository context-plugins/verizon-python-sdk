
# Ready Sim Device Id

## Structure

`ReadySimDeviceId`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `kind` | `str` | Optional | - |
| `id` | `str` | Optional | - |

## Example

```python
from verizon.models.ready_sim_device_id import ReadySimDeviceId

ready_sim_device_id = ReadySimDeviceId(
    kind='iccid',
    id='20-digit iccid'
)
```

