
# Campaign Software Upgrade

Software upgrade information.

## Structure

`CampaignSoftwareUpgrade`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `campaign_name` | `str` | Optional | Campaign name. |
| `software_name` | `str` | Required | Software name to upgrade to. |
| `software_from` | `str` | Required | Old software name. |
| `software_to` | `str` | Required | New software name. |
| `distribution_type` | `str` | Required | OMA or HTTP. |
| `start_date` | `date` | Required | Campaign start date. |
| `end_date` | `date` | Required | Campaign end date. |
| `download_after_date` | `date` | Optional | Specifies starting date client should download package. If null, client will download as soon as possible. |
| `download_time_window_list` | [`List[V2TimeWindow]`](../../doc/models/v2-time-window.md) | Optional | List of allowed download time windows. |
| `install_after_date` | `date` | Optional | Client will install package after date. If null, client will install as soon as possible. |
| `install_time_window_list` | [`List[V2TimeWindow]`](../../doc/models/v2-time-window.md) | Optional | List of allowed install time windows. |
| `device_list` | `List[str]` | Required | Device IMEI list. |

## Example

```python
import dateutil.parser

from verizon.models.campaign_software_upgrade import CampaignSoftwareUpgrade
from verizon.models.v2_time_window import V2TimeWindow

campaign_software_upgrade = CampaignSoftwareUpgrade(
    software_name='FOTA_Verizon_Model-A_02To03_HF',
    software_from='FOTA_Verizon_Model-A_00To01_HF',
    software_to='FOTA_Verizon_Model-A_02To03_HF',
    distribution_type='HTTP',
    start_date=dateutil.parser.parse('2020-08-21').date(),
    end_date=dateutil.parser.parse('2020-08-22').date(),
    device_list=[
        '990013907835573',
        '990013907884259'
    ],
    campaign_name='FOTA_Verizon_Upgrade',
    download_after_date=dateutil.parser.parse('2020-08-21').date(),
    download_time_window_list=[
        V2TimeWindow(
            start_time=20,
            end_time=21
        )
    ],
    install_after_date=dateutil.parser.parse('2020-08-21').date(),
    install_time_window_list=[
        V2TimeWindow(
            start_time=22,
            end_time=23
        )
    ]
)
```

