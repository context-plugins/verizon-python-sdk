
# Log Out Request

Request to end a Connectivity Management session.

## Structure

`LogOutRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `session_token` | `str` | Optional | The session token is returned to confirm that it was invalidated. |

## Example

```python
from verizon.models.log_out_request import LogOutRequest

log_out_request = LogOutRequest(
    session_token='bcce3ea6-fe4f-4952-bacf-eadd80718e83'
)
```

