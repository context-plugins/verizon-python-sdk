
# Target Authentication Body Host

Host information.

## Structure

`TargetAuthenticationBodyHost`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `hostandpath` | `str` | Optional | - |

## Example

```python
from verizon.models.target_authentication_body_host import TargetAuthenticationBodyHost

target_authentication_body_host = TargetAuthenticationBodyHost(
    hostandpath='https:// myhost.com:1825'
)
```

