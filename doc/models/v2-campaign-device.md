
# V2 Campaign Device

List of devices in a campaign.

## Structure

`V2CampaignDevice`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `total_device` | `int` | Optional | Total device count. |
| `has_more_data` | `bool` | Required | Has more report flag. |
| `last_seen_device_id` | `str` | Optional | Device identifier. |
| `max_page_size` | `int` | Required | Maximum page size. |
| `device_list` | [`List[V2DeviceStatus]`](../../doc/models/v2-device-status.md) | Required | List of devices with id in IMEI. |

## Example

```python
from verizon.models.v2_campaign_device import V2CampaignDevice
from verizon.models.v2_device_status import V2DeviceStatus

v2_campaign_device = V2CampaignDevice(
    has_more_data=True,
    max_page_size=1000,
    device_list=[
        V2DeviceStatus(
            device_id='15-digit IMEI',
            status='UpgradeSuccess',
            result_reason='DownloadInstallSucceeded'
        ),
        V2DeviceStatus(
            device_id='15-digit IMEI',
            status='UpgradeSuccess',
            result_reason='DownloadInstallSucceeded'
        ),
        V2DeviceStatus(
            device_id='15-digit IMEI',
            status='UpgradeSuccess',
            result_reason='DownloadInstallSucceeded'
        )
    ],
    total_device=1148,
    last_seen_device_id='15-digit IMEI'
)
```

