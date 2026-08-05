
# Device Labels

A label for a single device.

## Structure

`DeviceLabels`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `str` | Required | The label you want to associate with the device. |
| `value` | `str` | Required | The value of label |

## Example

```python
from verizon.models.device_labels import DeviceLabels

device_labels = DeviceLabels(
    name='VIN',
    value='XXUZL54B5YN105457'
)
```

