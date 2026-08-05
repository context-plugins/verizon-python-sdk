
# ESIM Device Id

## Structure

`ESIMDeviceId`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Optional | - |
| `kind` | `str` | Optional | - |

## Example

```python
from verizon.models.esim_device_id import ESIMDeviceId

e_sim_device_id = ESIMDeviceId(
    id='32-digit EID',
    kind='eid'
)
```

