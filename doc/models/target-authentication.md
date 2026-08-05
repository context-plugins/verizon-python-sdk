
# Target Authentication

OAuth 2 token and refresh token for TS to stream events to Target.

## Structure

`TargetAuthentication`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`TargetAuthenticationBody`](../../doc/models/target-authentication-body.md) | Optional | - |
| `version` | `str` | Optional | - |

## Example

```python
from verizon.models.target_authentication import TargetAuthentication
from verizon.models.target_authentication_body import TargetAuthenticationBody
from verizon.models.target_authentication_body_headers import TargetAuthenticationBodyHeaders
from verizon.models.target_authentication_body_host import TargetAuthenticationBodyHost

target_authentication = TargetAuthentication(
    body=TargetAuthenticationBody(
        grant_type='refresh_token',
        refresh_token='qfeqVjZTYzMmUtZWMzZqfq4ZDUtNzFhZWVkYTlmMjk1',
        scope='scope6',
        headers=TargetAuthenticationBodyHeaders(
            authorization='Basic RGFrqewfq2xpZW50QXBwVjI6YzM5YjqfqmI2LWI2MWQtNDRlZTQ5MmM1YTRk',
            content_type='application/x-www-form-urlencoded'
        ),
        host=TargetAuthenticationBodyHost(
            hostandpath='https:// myhost.com:1825'
        )
    ),
    version='1.0'
)
```

