
# V3 Campaign History

Campaign history.

## Structure

`V3CampaignHistory`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `has_more_data` | `bool` | Required | Has more report flag? |
| `last_seen_campaign_id` | `str` | Optional | Campaign identifier. |
| `campaign_list` | [`List[V3CampaignMetaInfo]`](../../doc/models/v3-campaign-meta-info.md) | Required | Firmware upgrade list. |

## Example

```python
import dateutil.parser

from verizon.models.campaign_meta_info_protocol_enum import CampaignMetaInfoProtocolEnum
from verizon.models.v3_campaign_history import V3CampaignHistory
from verizon.models.v3_campaign_meta_info import V3CampaignMetaInfo
from verizon.models.v3_time_window import V3TimeWindow

v3_campaign_history = V3CampaignHistory(
    has_more_data=True,
    campaign_list=[
        V3CampaignMetaInfo(
            account_name='0000123456-00001',
            id='60b5d639-ccdc-4db8-8824-069bd94c95bf',
            make='Verizon',
            model='Model-A',
            start_date=dateutil.parser.parse('2020-08-21').date(),
            end_date=dateutil.parser.parse('2020-08-22').date(),
            status='CampaignEnded',
            campaign_name='FOTA_Verizon_Upgrade',
            firmware_name='firmwareName6',
            firmware_from='firmwareFrom6',
            firmware_to='firmwareTo6',
            protocol=CampaignMetaInfoProtocolEnum.LW_M2M,
            campaign_time_window_list=[
                V3TimeWindow(
                    start_time=20,
                    end_time=21
                )
            ]
        )
    ],
    last_seen_campaign_id='60b5d639-ccdc-4db8-8824-069bd94c95bf'
)
```

