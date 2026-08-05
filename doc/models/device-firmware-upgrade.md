
# Device Firmware Upgrade

Firmware upgrades information.

## Structure

`DeviceFirmwareUpgrade`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `device_id` | `str` | Required | Device identifier. |
| `campaign_id` | `str` | Required | Campaign identifier. |
| `account_name` | `str` | Required | Account identifier. |
| `firmware_name` | `str` | Optional | Firmware name. |
| `firmware_from` | `str` | Optional | Old firmware version. |
| `firmware_to` | `str` | Optional | New firmware version. |
| `start_date` | `date` | Required | Firmware upgrade start date. |
| `status` | `str` | Required | Firmware upgrade status. |
| `reason` | `str` | Required | Software upgrade result reason. |
| `report_updated_time` | `str` | Optional | Report updated time. |

## Example

```python
import dateutil.parser

from verizon.models.device_firmware_upgrade import DeviceFirmwareUpgrade

device_firmware_upgrade = DeviceFirmwareUpgrade(
    device_id='15-digit IMEI',
    campaign_id='252d7ffc-7e35-11ec-931d-76f56843c393',
    account_name='0000123456-00001',
    start_date=dateutil.parser.parse('2022-01-25').date(),
    status='UpgradeSuccess',
    reason='Upgrade completed successfully',
    firmware_name='SEQUANSCommunications_GM01Q_SR1.2.0.0-10657_SR1.2.0.0-10512',
    firmware_from='SR1.2.0.0-10657',
    firmware_to='SR1.2.0.0-10512',
    report_updated_time='2022-01-26 03:45:01.608 +0000 UTC'
)
```

