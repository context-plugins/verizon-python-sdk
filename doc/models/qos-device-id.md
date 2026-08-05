
# Qos Device Id

## Structure

`QosDeviceId`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Optional | - |
| `kind` | `str` | Optional | - |

## Example

```python
from verizon.models.qos_device_id import QosDeviceId

qos_device_id = QosDeviceId(
    id='10-digit phone number',
    kind='mdn'
)
```

