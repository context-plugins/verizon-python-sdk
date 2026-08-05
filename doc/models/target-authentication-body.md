
# Target Authentication Body

## Structure

`TargetAuthenticationBody`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `grant_type` | `str` | Optional | Authentication grant type. |
| `refresh_token` | `str` | Optional | Refresh token. |
| `scope` | `str` | Optional | Authentication scopes. |
| `headers` | [`TargetAuthenticationBodyHeaders`](../../doc/models/target-authentication-body-headers.md) | Optional | Authentication headers. |
| `host` | [`TargetAuthenticationBodyHost`](../../doc/models/target-authentication-body-host.md) | Optional | Host information. |

## Example

```python
from verizon.models.target_authentication_body import TargetAuthenticationBody
from verizon.models.target_authentication_body_headers import TargetAuthenticationBodyHeaders
from verizon.models.target_authentication_body_host import TargetAuthenticationBodyHost

target_authentication_body = TargetAuthenticationBody(
    grant_type='refresh_token',
    refresh_token='qfeqVjZTYzMmUtZWMzZqfq4ZDUtNzFhZWVkYTlmMjk1',
    scope='scope8',
    headers=TargetAuthenticationBodyHeaders(
        authorization='Basic RGFrqewfq2xpZW50QXBwVjI6YzM5YjqfqmI2LWI2MWQtNDRlZTQ5MmM1YTRk',
        content_type='application/x-www-form-urlencoded'
    ),
    host=TargetAuthenticationBodyHost(
        hostandpath='https:// myhost.com:1825'
    )
)
```

