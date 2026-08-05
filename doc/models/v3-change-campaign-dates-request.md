
# V3 Change Campaign Dates Request

Campaign dates and time windows.

## Structure

`V3ChangeCampaignDatesRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `start_date` | `date` | Required | Campaign start date. |
| `end_date` | `date` | Required | Campaign end date. |
| `campaign_time_window_list` | [`List[V3TimeWindow]`](../../doc/models/v3-time-window.md) | Optional | List of allowed campaign time windows. |

## Example

```python
import dateutil.parser

from verizon.models.v3_change_campaign_dates_request import V3ChangeCampaignDatesRequest
from verizon.models.v3_time_window import V3TimeWindow

v3_change_campaign_dates_request = V3ChangeCampaignDatesRequest(
    start_date=dateutil.parser.parse('2022-02-23').date(),
    end_date=dateutil.parser.parse('2022-02-24').date(),
    campaign_time_window_list=[
        V3TimeWindow(
            start_time=14,
            end_time=18
        )
    ]
)
```

