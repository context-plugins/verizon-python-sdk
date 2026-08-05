
# V3 Campaign Device

Campaign history.

## Structure

`V3CampaignDevice`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `total_device` | `int` | Optional | Total device count. |
| `has_more_data` | `bool` | Required | Has more report flag. |
| `last_seen_device_id` | `str` | Optional | Device identifier. |
| `max_page_size` | `int` | Required | Maximum page size. |
| `device_list` | [`List[V3DeviceStatus]`](../../doc/models/v3-device-status.md) | Required | List of devices with id in IMEI. |

## Example

```python
import dateutil.parser

from verizon.models.v3_campaign_device import V3CampaignDevice
from verizon.models.v3_device_status import V3DeviceStatus

v3_campaign_device = V3CampaignDevice(
    has_more_data=True,
    max_page_size=1000,
    device_list=[
        V3DeviceStatus(
            device_id='15-digit IMEI',
            status='UpgradePending',
            result_reason='Upgrade pending, the device upgrade is estimated to be scheduled for 06 Oct 22 18:05 UTC',
            updated_time=dateutil.parser.parse('2022-08-05T21:05:27.129Z'),
            recent_attempt_time=dateutil.parser.parse('2022-10-05T21:05:01.19Z'),
            next_attempt_time=dateutil.parser.parse('2022-10-06T18:35:00Z')
        )
    ],
    total_device=2689,
    last_seen_device_id='15-digit IMEI'
)
```

