
# Device IMEI

Device IMEI list.

## Structure

`DeviceIMEI`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `device_list` | `List[str]` | Required | Device IMEI list. |

## Example

```python
from verizon.models.device_imei import DeviceIMEI

device_imei = DeviceIMEI(
    device_list=[
        '15-digit IMEI'
    ]
)
```

