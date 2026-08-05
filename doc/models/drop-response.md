
# Drop Response

## Structure

`DropResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `items` | [`List[DropResponseItem]`](../../doc/models/drop-response-item.md) | Optional | - |

## Example

```python
from verizon.models.drop_response import DropResponse
from verizon.models.drop_response_item import DropResponseItem

drop_response = DropResponse(
    items=[
        DropResponseItem(
            imei='imei8'
        )
    ]
)
```

