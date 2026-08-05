
# Log In Request

Request to initiate a Connectivity Management session and returns a VZ-M2M session token that is required in subsequent API requests.

## Structure

`LogInRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `username` | `str` | Required | The username for authentication. |
| `password` | `str` | Required | The password for authentication. |

## Example

```python
from verizon.models.log_in_request import LogInRequest

log_in_request = LogInRequest(
    username='zbeeblebrox',
    password='IMgr8'
)
```

