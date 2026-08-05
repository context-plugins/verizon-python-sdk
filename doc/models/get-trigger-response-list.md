
# Get Trigger Response List

## Structure

`GetTriggerResponseList`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `triggers` | [`List[GetTriggerResponse]`](../../doc/models/get-trigger-response.md) | Optional | **Constraints**: *Maximum Items*: `3` |

## Example

```python
import dateutil.parser

from verizon.models.get_trigger_response import GetTriggerResponse
from verizon.models.get_trigger_response_list import GetTriggerResponseList

get_trigger_response_list = GetTriggerResponseList(
    triggers=[
        GetTriggerResponse(
            account_name='accountName4',
            comparator='comparator2',
            created_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
            group_name='groupName0',
            modified_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z')
        ),
        GetTriggerResponse(
            account_name='accountName4',
            comparator='comparator2',
            created_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
            group_name='groupName0',
            modified_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z')
        ),
        GetTriggerResponse(
            account_name='accountName4',
            comparator='comparator2',
            created_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
            group_name='groupName0',
            modified_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z')
        )
    ]
)
```

