
# Firmware Upgrade Change Result

Upgrade information.

## Structure

`FirmwareUpgradeChangeResult`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `str` | Optional | Account identifier in "##########-#####". |
| `id` | `str` | Optional | The unique identifier for this upgrade. |
| `device_list` | [`List[V1DeviceListItem]`](../../doc/models/v1-device-list-item.md) | Optional | A JSON object for each device that was included in the request, showing the device IMEI, the status of the addition or removal, and additional information about the status. |

## Example

```python
from verizon.models.firmware_upgrade_change_result import FirmwareUpgradeChangeResult
from verizon.models.v1_device_list_item import V1DeviceListItem

firmware_upgrade_change_result = FirmwareUpgradeChangeResult(
    account_name='0000123456-00001',
    id='60b5d639-ccdc-4db8-8824-069bd94c95bf',
    device_list=[
        V1DeviceListItem(
            device_id='15-digit IMEI',
            status='AddDeviceSucceed',
            reason='Device added Successfully'
        ),
        V1DeviceListItem(
            device_id='15-digit IMEI',
            status='AddDeviceSucceed',
            reason='Device added Successfully'
        )
    ]
)
```

