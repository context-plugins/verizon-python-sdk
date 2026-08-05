
# V2 Campaign Meta Info

Campaign and campaign details.

## Structure

`V2CampaignMetaInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `str` | Required | Account identifier. |
| `id` | `str` | Required | Campaign identifier. |
| `campaign_name` | `str` | Optional | Campaign name. |
| `software_name` | `str` | Required | Software name. |
| `distribution_type` | `str` | Required | LWM2M, OMD-DM or HTTP. |
| `software_from` | `str` | Required | Old software name. |
| `software_to` | `str` | Required | New software name. |
| `make` | `str` | Required | Applicable make. |
| `model` | `str` | Required | Applicable model. |
| `start_date` | `date` | Required | Campaign start date. |
| `end_date` | `date` | Required | Campaign end date. |
| `download_after_date` | `date` | Optional | Specifies starting date client should download package. If null, client will download as soon as possible. |
| `download_time_window_list` | [`List[V2TimeWindow]`](../../doc/models/v2-time-window.md) | Optional | List of allowed download time windows. |
| `install_after_date` | `date` | Optional | Client will install package after date. If null, client will install as soon as possible. |
| `install_time_window_list` | [`List[V2TimeWindow]`](../../doc/models/v2-time-window.md) | Optional | List of allowed install time windows. |
| `status` | `str` | Required | Software upgrade status. |

## Example

```python
import dateutil.parser

from verizon.models.v2_campaign_meta_info import V2CampaignMetaInfo
from verizon.models.v2_time_window import V2TimeWindow

v2_campaign_meta_info = V2CampaignMetaInfo(
    account_name='0402196254-00001',
    id='60b5d639-ccdc-4db8-8824-069bd94c95bf',
    software_name='FOTA_Verizon_Model-A_02To03_HF',
    distribution_type='HTTP',
    software_from='FOTA_Verizon_Model-A_00To01_HF',
    software_to='FOTA_Verizon_Model-A_02To03_HF',
    make='Verizon',
    model='Model-A',
    start_date=dateutil.parser.parse('2020-08-21').date(),
    end_date=dateutil.parser.parse('2020-08-22').date(),
    status='CampaignEnded',
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

