
# V1 Device List Item

A JSON object for each device that was included in the request, showing the device IMEI, the status of the addition or removal, and additional information about the status.

## Structure

`V1DeviceListItem`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `device_id` | `str` | Optional | Device IMEI. |
| `status` | `str` | Optional | Whether the device was successfully added or removed from the campaign. |
| `reason` | `str` | Optional | Additional details about the status. |

## Example

```python
from verizon.models.v1_device_list_item import V1DeviceListItem

v1_device_list_item = V1DeviceListItem(
    device_id='900000000000001',
    status='LicenseAssignSuccess',
    reason='Success'
)
```

