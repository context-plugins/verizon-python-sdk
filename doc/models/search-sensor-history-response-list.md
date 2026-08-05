
# Search Sensor History Response List

A success response includes an array of all matching events.

## Structure

`SearchSensorHistoryResponseList`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `search_sensor_history` | [`List[SearchDeviceResponse]`](../../doc/models/search-device-response.md) | Optional | **Constraints**: *Maximum Items*: `100` |

## Example

```python
from verizon.models.fields_2 import Fields2
from verizon.models.search_device_response import SearchDeviceResponse
from verizon.models.search_sensor_history_response_list import SearchSensorHistoryResponseList

search_sensor_history_response_list = SearchSensorHistoryResponseList(
    search_sensor_history=[
        SearchDeviceResponse(
            action='action6',
            createdon='createdon6',
            deviceid='deviceid6',
            fields=Fields2(
                temperature='temperature0'
            ),
            id='id6'
        ),
        SearchDeviceResponse(
            action='action6',
            createdon='createdon6',
            deviceid='deviceid6',
            fields=Fields2(
                temperature='temperature0'
            ),
            id='id6'
        ),
        SearchDeviceResponse(
            action='action6',
            createdon='createdon6',
            deviceid='deviceid6',
            fields=Fields2(
                temperature='temperature0'
            ),
            id='id6'
        )
    ]
)
```

