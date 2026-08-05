
# Campaign Status Enum

Current status of the campaign.

## Enumeration

`CampaignStatusEnum`

## Fields

| Name |
|  --- |
| `CAMPAIGNREQUESTPENDING` |
| `CAMPAIGNREQUESTFAILED` |
| `CAMPAIGNREQUESTQUEUED` |
| `CAMPAIGNCANCELLED` |
| `CAMPAIGNABORTED` |
| `CAMPAIGNFAILED` |
| `CAMPAIGNSCHEDULED` |
| `CAMPAIGNENDED` |

## Example

```python
from verizon.models.campaign_status_enum import CampaignStatusEnum

campaign_status = CampaignStatusEnum.CAMPAIGNREQUESTPENDING
```

