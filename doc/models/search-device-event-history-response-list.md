
# Search Device Event History Response List

A success response includes an array of all matching events.

## Structure

`SearchDeviceEventHistoryResponseList`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `search_device_event_history` | [`List[SearchDeviceResponse]`](../../doc/models/search-device-response.md) | Optional | **Constraints**: *Maximum Items*: `100` |

## Example

```python
from verizon.models.fields_2 import Fields2
from verizon.models.search_device_event_history_response_list import SearchDeviceEventHistoryResponseList
from verizon.models.search_device_response import SearchDeviceResponse

search_device_event_history_response_list = SearchDeviceEventHistoryResponseList(
    search_device_event_history=[
        SearchDeviceResponse(
            action='action4',
            createdon='createdon4',
            deviceid='deviceid8',
            fields=Fields2(
                temperature='temperature0'
            ),
            id='id8'
        )
    ]
)
```

