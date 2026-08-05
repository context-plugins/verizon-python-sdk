
# Campaign Firmware Upgrade

Firmware upgrade for devices.

## Structure

`CampaignFirmwareUpgrade`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `campaign_name` | `str` | Optional | Campaign name. |
| `firmware_name` | `str` | Required | Firmware name to upgrade to. |
| `firmware_from` | `str` | Required | Old firmware version. |
| `firmware_to` | `str` | Required | New firmware version. |
| `protocol` | `str` | Required | Valid values include: LWM2M, OMA and HTTP.<br><br>**Default**: `"LWM2M"` |
| `start_date` | `date` | Required | Campaign start date. |
| `end_date` | `date` | Required | Campaign end date. |
| `campaign_time_window_list` | [`List[V3TimeWindow]`](../../doc/models/v3-time-window.md) | Optional | List of allowed campaign time windows. |
| `device_list` | `List[str]` | Required | Device IMEI list. |
| `auto_assign_license_flag` | `bool` | Required | This flag, when set to true, will assign a FOTA license automatically if the device does not have one already. |
| `auto_add_devices_flag` | `bool` | Required | this flag, when set to true, will automatically add a device of the same make and model to a campaign. |

## Example

```python
import dateutil.parser

from verizon.models.campaign_firmware_upgrade import CampaignFirmwareUpgrade
from verizon.models.v3_time_window import V3TimeWindow

campaign_firmware_upgrade = CampaignFirmwareUpgrade(
    firmware_name='SEQUANSCommunications_GM01Q_SR1.2.0.0-10512_SR1.2.0.0-10657',
    firmware_from='SR1.2.0.0-10512',
    firmware_to='SR1.2.0.0-10657',
    protocol='LWM2M',
    start_date=dateutil.parser.parse('2021-09-29').date(),
    end_date=dateutil.parser.parse('2021-10-01').date(),
    device_list=[
        '15-digit IMEI'
    ],
    auto_assign_license_flag=False,
    auto_add_devices_flag=False,
    campaign_name='Smart FOTA - test 4',
    campaign_time_window_list=[
        V3TimeWindow(
            start_time=18,
            end_time=22
        )
    ]
)
```

