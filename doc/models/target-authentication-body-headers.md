
# Target Authentication Body Headers

Authentication headers.

## Structure

`TargetAuthenticationBodyHeaders`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `authorization` | `str` | Optional | Authorization header. |
| `content_type` | `str` | Optional | Content-Type header. |

## Example

```python
from verizon.models.target_authentication_body_headers import TargetAuthenticationBodyHeaders

target_authentication_body_headers = TargetAuthenticationBodyHeaders(
    authorization='Basic RGFrqewfq2xpZW50QXBwVjI6YzM5YjqfqmI2LWI2MWQtNDRlZTQ5MmM1YTRk',
    content_type='application/x-www-form-urlencoded'
)
```

