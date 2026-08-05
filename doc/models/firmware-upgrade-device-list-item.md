
# Firmware Upgrade Device List Item

A JSON object for each device that was included in the upgrade, showing the device IMEI, the status of the upgrade, and additional information about the status.

## Structure

`FirmwareUpgradeDeviceListItem`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `device_id` | `str` | Optional | Device IMEI. |
| `status` | `str` | Optional | The status of the upgrade for this device. |
| `result_reason` | `str` | Optional | Additional details about the status. Not included when status='Request Pending.' |

## Example

```python
from verizon.models.firmware_upgrade_device_list_item import FirmwareUpgradeDeviceListItem

firmware_upgrade_device_list_item = FirmwareUpgradeDeviceListItem(
    device_id='900000000000002',
    status='Device Accepted',
    result_reason='success'
)
```

