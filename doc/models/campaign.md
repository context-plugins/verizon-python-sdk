
# Campaign

Firmware upgrade information.

## Structure

`Campaign`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Required | Upgrade identifier. |
| `account_name` | `str` | Required | Account identifier. |
| `campaign_name` | `str` | Optional | Campaign name. |
| `firmware_name` | `str` | Optional | Name of firmware. |
| `firmware_from` | `str` | Optional | Old firmware version. |
| `firmware_to` | `str` | Optional | New firmware version. |
| `protocol` | `str` | Required | The protocol of the firmware distribution. Default: LWM2M.<br><br>**Default**: `"LWM2M"` |
| `make` | `str` | Required | Applicable make. |
| `model` | `str` | Required | Applicable model. |
| `start_date` | `date` | Required | Campaign start date. |
| `end_date` | `date` | Required | Campaign end date. |
| `campaign_time_window_list` | [`List[V3TimeWindow]`](../../doc/models/v3-time-window.md) | Optional | List of allowed campaign time windows. |
| `status` | `str` | Required | Firmware upgrade status. |
| `auto_assign_license_flag` | `bool` | Required | Any device included in the device list which does not have a license will automatically be assigned a FOTA license, assuming there are enough FOTA licenses available, when set to true. |
| `auto_add_devices_flag` | `bool` | Required | Beyond the devices included on the device list, any other device(s) which matches the eligibility criteria (same make, model, current firmware, protocol, billing account) will automatically be added to the campaign list during the life of the campaign when set to true. |

## Example

```python
import dateutil.parser

from verizon.models.campaign import Campaign
from verizon.models.v3_time_window import V3TimeWindow

campaign = Campaign(
    id='f858b8c4-2153-11ec-8c44-aeb16d1aa652',
    account_name='0642233522-00001',
    protocol='LWM2M',
    make='SEQUANS Communications',
    model='GM01Q',
    start_date=dateutil.parser.parse('2021-09-29').date(),
    end_date=dateutil.parser.parse('2021-10-01').date(),
    status='CampaignPreScheduled',
    auto_assign_license_flag=False,
    auto_add_devices_flag=False,
    campaign_name='Smart FOTA - test 4',
    firmware_name='SEQUANSCommunications_GM01Q_SR1.2.0.0-10512_SR1.2.0.0-10657',
    firmware_from='SR1.2.0.0-10512',
    firmware_to='SR1.2.0.0-10657',
    campaign_time_window_list=[
        V3TimeWindow(
            start_time=18,
            end_time=22
        )
    ]
)
```

