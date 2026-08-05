
# V3 Device List Item

Device changed.

## Structure

`V3DeviceListItem`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `device_id` | `str` | Optional | Device IMEI. |
| `status` | `str` | Optional | Success or failure. |
| `reason` | `str` | Optional | Result reason. |

## Example

```python
from verizon.models.v3_device_list_item import V3DeviceListItem

v3_device_list_item = V3DeviceListItem(
    device_id='15-digit IMEI',
    status='AddDeviceSucceed',
    reason='Device added Successfully'
)
```

