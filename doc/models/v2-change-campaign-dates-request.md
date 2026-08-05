
# V2 Change Campaign Dates Request

New dates and time windows.

## Structure

`V2ChangeCampaignDatesRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `start_date` | `date` | Required | Campaign start date. |
| `end_date` | `date` | Required | Campaign end date. |
| `download_after_date` | `date` | Optional | Specifies starting date client should download package. If null, client will download as soon as possible. |
| `download_time_window_list` | [`List[V2TimeWindow]`](../../doc/models/v2-time-window.md) | Optional | List of allowed download time windows. Removing of existing windows is not allowed. |
| `install_after_date` | `date` | Optional | Client will install package after date. If null, client will install as soon as possible. |
| `install_time_window_list` | [`List[V2TimeWindow]`](../../doc/models/v2-time-window.md) | Optional | List of allowed install time windows. Removing of existing windows is not allowed. |

## Example

```python
import dateutil.parser

from verizon.models.v2_change_campaign_dates_request import V2ChangeCampaignDatesRequest
from verizon.models.v2_time_window import V2TimeWindow

v2_change_campaign_dates_request = V2ChangeCampaignDatesRequest(
    start_date=dateutil.parser.parse('2020-08-21').date(),
    end_date=dateutil.parser.parse('2020-08-22').date(),
    download_after_date=dateutil.parser.parse('2020-08-21').date(),
    download_time_window_list=[
        V2TimeWindow(
            start_time=3,
            end_time=4
        )
    ],
    install_after_date=dateutil.parser.parse('2020-08-21').date(),
    install_time_window_list=[
        V2TimeWindow(
            start_time=5,
            end_time=6
        )
    ]
)
```

