
# Firmware Upgrade

Array of upgrade objects with the specified status.

## Structure

`FirmwareUpgrade`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Optional | The unique identifier for this upgrade. |
| `account_name` | `str` | Optional | Account identifier in "##########-#####". |
| `firmware_name` | `str` | Optional | The name of the firmware image that will be used for the upgrade. |
| `firmware_to` | `str` | Optional | The name of the firmware version that will be on the devices after a successful upgrade. |
| `start_date` | `str` | Optional | The intended start date for the upgrade. |
| `status` | `str` | Optional | The current status of the upgrade. |
| `device_list` | [`List[FirmwareUpgradeDeviceListItem]`](../../doc/models/firmware-upgrade-device-list-item.md) | Optional | A JSON object for each device that was included in the upgrade, showing the device IMEI, the status of the upgrade, and additional information about the status. |

## Example

```python
from verizon.models.firmware_upgrade import FirmwareUpgrade
from verizon.models.firmware_upgrade_device_list_item import FirmwareUpgradeDeviceListItem

firmware_upgrade = FirmwareUpgrade(
    id='60b5d639-ccdc-4db8-8824-069bd94c95bf',
    account_name='0402196254-00001',
    firmware_name='FOTA_Verizon_Model-A_01To02_HF',
    firmware_to='VerizonFirmwareVersion-02',
    start_date='2018-04-01',
    status='Queued',
    device_list=[
        FirmwareUpgradeDeviceListItem(
            device_id='900000000000002',
            status='Device Accepted',
            result_reason='success'
        ),
        FirmwareUpgradeDeviceListItem(
            device_id='900000000000003',
            status='Device Accepted',
            result_reason='success'
        )
    ]
)
```

