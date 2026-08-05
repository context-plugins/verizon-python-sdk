
# Generate Response

## Structure

`GenerateResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `items` | [`List[GenerateResponseItem]`](../../doc/models/generate-response-item.md) | Optional | - |

## Example

```python
from verizon.models.generate_response import GenerateResponse
from verizon.models.generate_response_item import GenerateResponseItem
from verizon.models.generate_response_item_credential import GenerateResponseItemCredential

generate_response = GenerateResponse(
    items=[
        GenerateResponseItem(
            imei='imei8',
            credential=GenerateResponseItemCredential(
                username='username6',
                password='password0'
            )
        ),
        GenerateResponseItem(
            imei='imei8',
            credential=GenerateResponseItemCredential(
                username='username6',
                password='password0'
            )
        ),
        GenerateResponseItem(
            imei='imei8',
            credential=GenerateResponseItemCredential(
                username='username6',
                password='password0'
            )
        )
    ]
)
```

