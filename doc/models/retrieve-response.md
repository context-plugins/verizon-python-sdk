
# Retrieve Response

## Structure

`RetrieveResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `items` | [`List[RetrieveResponseItem]`](../../doc/models/retrieve-response-item.md) | Optional | - |

## Example

```python
from verizon.models.retrieve_response import RetrieveResponse
from verizon.models.retrieve_response_item import RetrieveResponseItem

retrieve_response = RetrieveResponse(
    items=[
        RetrieveResponseItem(
            imei='imei8',
            username='username2',
            failure='failure8'
        )
    ]
)
```

