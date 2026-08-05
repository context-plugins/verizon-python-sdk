
# Device Info

The devices that you want to locate. The array cannot contain more than 20 devices.

## Structure

`DeviceInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Required | Device identifier. |
| `kind` | `str` | Required | Device identifier kind. |
| `mdn` | `str` | Required | Device MDN. |

## Example

```python
from verizon.models.device_info import DeviceInfo

device_info = DeviceInfo(
    id='980003420535573',
    kind='imei',
    mdn='7892345678'
)
```

