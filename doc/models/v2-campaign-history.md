
# V2 Campaign History

Campaign history details.

## Structure

`V2CampaignHistory`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `has_more_data` | `bool` | Required | Has more report flag. |
| `last_seen_campaign_id` | `str` | Optional | Campaign identifier. |
| `campaign_list` | [`List[V2CampaignMetaInfo]`](../../doc/models/v2-campaign-meta-info.md) | Required | Software upgrade list. |

## Example

```python
import dateutil.parser

from verizon.models.v2_campaign_history import V2CampaignHistory
from verizon.models.v2_campaign_meta_info import V2CampaignMetaInfo
from verizon.models.v2_time_window import V2TimeWindow

v2_campaign_history = V2CampaignHistory(
    has_more_data=True,
    campaign_list=[
        V2CampaignMetaInfo(
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
    ],
    last_seen_campaign_id='60b5d639-ccdc-4db8-8824-069bd94c95bf'
)
```

