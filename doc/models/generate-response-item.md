
# Generate Response Item

## Structure

`GenerateResponseItem`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `imei` | `str` | Optional | - |
| `credential` | [`GenerateResponseItemCredential`](../../doc/models/generate-response-item-credential.md) | Optional | - |

## Example

```python
from verizon.models.generate_response_item import GenerateResponseItem
from verizon.models.generate_response_item_credential import GenerateResponseItemCredential

generate_response_item = GenerateResponseItem(
    imei='100096454851324',
    credential=GenerateResponseItemCredential(
        username='username6',
        password='password0'
    )
)
```

