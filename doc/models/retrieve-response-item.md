
# Retrieve Response Item

## Structure

`RetrieveResponseItem`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `imei` | `str` | Optional | - |
| `username` | `str` | Optional | Present if credentials exist |
| `failure` | `str` | Optional | Present if retrieval failed |

## Example

```python
from verizon.models.retrieve_response_item import RetrieveResponseItem

retrieve_response_item = RetrieveResponseItem(
    imei='100096454851324',
    username='290sk9vmybmxi1kmx1kxo8w13u',
    failure='No active username'
)
```

