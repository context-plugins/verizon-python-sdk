
# Firmware Campaign

Firmware upgrade information.

## Structure

`FirmwareCampaign`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Required | Upgrade identifier. |
| `account_name` | `str` | Required | Account identifier. |
| `campaign_name` | `str` | Optional | Campaign name. |
| `firmware_name` | `str` | Optional | Firmware name (for firmware upgrade only). |
| `firmware_from` | `str` | Required | Old firmware version (for firmware upgrade only). |
| `firmware_to` | `str` | Required | New firmware version (for firmware upgrade only). |
| `protocol` | `str` | Required | Available values: LWM2M.<br><br>**Default**: `"LWM2M"` |
| `make` | `str` | Required | - |
| `model` | `str` | Required | - |
| `start_date` | `date` | Required | Campaign start date. |
| `end_date` | `date` | Required | Campaign end date. |
| `campaign_time_window_list` | [`List[V3TimeWindow]`](../../doc/models/v3-time-window.md) | Optional | List of allowed campaign time windows. |
| `status` | `str` | Required | Campaign status. |

## Example

```python
import dateutil.parser

from verizon.models.firmware_campaign import FirmwareCampaign
from verizon.models.v3_time_window import V3TimeWindow

firmware_campaign = FirmwareCampaign(
    id='f858b8c4-2153-11ec-8c44-aeb16d1aa652',
    account_name='0000123456-00001',
    firmware_from='SR1.2.0.0-10512',
    firmware_to='SR1.2.0.0-10657',
    protocol='LWM2M',
    make='SEQUANS Communications',
    model='GM01Q',
    start_date=dateutil.parser.parse('2021-09-29').date(),
    end_date=dateutil.parser.parse('2021-10-01').date(),
    status='CampaignRequestPending',
    campaign_name='Smart FOTA - test 4',
    firmware_name='SEQUANSCommunications_GM01Q_SR1.2.0.0-10512_SR1.2.0.0-10657',
    campaign_time_window_list=[
        V3TimeWindow(
            start_time=18,
            end_time=22
        )
    ]
)
```

