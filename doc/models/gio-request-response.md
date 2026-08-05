
# GIO Request Response

## Structure

`GIORequestResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `request_id` | `str` | Optional | **Constraints**: *Minimum Length*: `3`, *Maximum Length*: `64`, *Pattern*: `^[A-Za-z0-9\-]{3,64}$` |

## Example

```python
from verizon.models.gio_request_response import GIORequestResponse

gio_request_response = GIORequestResponse(
    request_id='d1f08526-5443-4054-9a29-4456490ea9f8'
)
```

