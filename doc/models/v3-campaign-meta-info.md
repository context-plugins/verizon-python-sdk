
# V3 Campaign Meta Info

Campaign and campaign details.

## Structure

`V3CampaignMetaInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `str` | Required | Account identifier. |
| `id` | `str` | Required | Campaign identifier. |
| `campaign_name` | `str` | Optional | Campaign name. |
| `firmware_name` | `str` | Optional | Firmware name. |
| `firmware_from` | `str` | Optional | Old firmware version. |
| `firmware_to` | `str` | Optional | New software version. |
| `protocol` | [`CampaignMetaInfoProtocolEnum`](../../doc/models/campaign-meta-info-protocol-enum.md) | Optional | Firmware protocol. Valid values include: LWM2M, OMD-DM.<br><br>**Default**: `"LWM2M"` |
| `make` | `str` | Required | Device make. |
| `model` | `str` | Required | Device model. |
| `start_date` | `date` | Required | Campaign start date. |
| `end_date` | `date` | Required | Campaign end date. |
| `campaign_time_window_list` | [`List[V3TimeWindow]`](../../doc/models/v3-time-window.md) | Optional | List of allowed campaign time windows. |
| `status` | `str` | Required | Firmware upgrade status. |

## Example

```python
import dateutil.parser

from verizon.models.campaign_meta_info_protocol_enum import CampaignMetaInfoProtocolEnum
from verizon.models.v3_campaign_meta_info import V3CampaignMetaInfo
from verizon.models.v3_time_window import V3TimeWindow

v3_campaign_meta_info = V3CampaignMetaInfo(
    account_name='0000123456-00001',
    id='60b5d639-ccdc-4db8-8824-069bd94c95bf',
    make='Verizon',
    model='Model-A',
    start_date=dateutil.parser.parse('2020-08-21').date(),
    end_date=dateutil.parser.parse('2020-08-22').date(),
    status='CampaignEnded',
    campaign_name='FOTA_Verizon_Upgrade',
    firmware_name='FOTA_Verizon_Model-A_02To03_HF',
    firmware_from='FOTA_Verizon_Model-A_00To01_HF',
    firmware_to='FOTA_Verizon_Model-A_02To03_HF',
    protocol=CampaignMetaInfoProtocolEnum.LW_M2M,
    campaign_time_window_list=[
        V3TimeWindow(
            start_time=20,
            end_time=21
        )
    ]
)
```

